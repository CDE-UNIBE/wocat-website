from uuid import uuid4

from django.core.exceptions import ValidationError
from django.forms import CharField, TextInput
from django.forms.utils import ErrorList
from django.template.defaultfilters import filesizeformat, slugify
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.utils.html import format_html, mark_safe
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.blocks import RawHTMLBlock, PageChooserBlock, BooleanBlock, ChoiceBlock, \
    StreamBlock, ListBlock, StructBlock, CharBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock as WagtailEmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock

from wocat.medialibrary.blocks import MediaTeaserBlock
from wocat.news.blocks import NewsTeaserBlock
from wocat.users.blocks import UserTeaserBlock, CONTACT_PERSON_TEASER_BLOCKS


class HeadingBlock(blocks.CharBlock):
    class Meta:
        classname = 'full title'
        icon = 'title'
        template = 'widgets/heading3.html'

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        context['text'] = value
        return context


class RichTextBlock(blocks.RichTextBlock):
    class Meta:
        icon = 'pilcrow'
        template = 'widgets/richtext.html'

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        context['content'] = value
        return context


class ImageBlock(ImageChooserBlock):
    class Meta:
        icon = 'image'
        template = 'widgets/image.html'

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        if value:
            context['src'] = value.get_rendition('max-1200x1200').url
            context['name'] = value.title
        return context


class EmbedBlock(WagtailEmbedBlock):
    class Meta:
        icon = 'media'
        template = 'widgets/embed.html'

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        context['embed'] = value
        return context


BASE_BLOCKS = [
    ('heading', HeadingBlock()),
    ('rich_text', RichTextBlock()),
    ('image', ImageBlock()),
    ('embed', EmbedBlock()),
]


class LinkBlock(StructBlock):
    name = blocks.CharBlock(required=False)
    page = PageChooserBlock(required=False)
    link = blocks.URLBlock(required=False)

    def __init__(self, required=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.required = required

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        page = value.get('page')
        link = value.get('link')
        context.update({
            'href': page.url if page else link,
            'external': not bool(page),
            'text': value.get('name') or _('read more'),
        })
        return context

    def clean(self, value):
        at_lest_one_field_required_fields = ['page', 'url']
        if self.required and not any([bool(value.get(field)) for field in at_lest_one_field_required_fields]):
            error_message = _('At lest one of {} is required').format(at_lest_one_field_required_fields)
            errors = {field: ErrorList([error_message]) for field in at_lest_one_field_required_fields}
            raise ValidationError(error_message, params=errors)
        return super().clean(value)


class DocumentBlock(DocumentChooserBlock):
    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        document = value
        if not document:
            return context
        context.update({
            'title': document.title,
            'fileurl': document.url,
            'filename': document.filename,
            'filesize': filesizeformat(document.file.size),
            'owner': document.uploaded_by_user,
            'type': document.file_extension,
        })
        return context

    def render(self, value, context=None):
        # Add the file_delete_url if the current user is owner.
        if value and context:
            user = context.get('user')
            # check permission: "user is owner and document is not older than a day"
            if user and user == value.uploaded_by_user and \
                        value.created_at + timezone.timedelta(days=1) > timezone.now():
                delete_url = reverse('cms:upload-delete', kwargs={'document_id': value.id})
                context['file_delete_url'] = delete_url
        return super().render(value, context)

    class Meta:
        icon = "doc-empty"
        template = 'widgets/file-link.html'


class ReadMoreBlock(StructBlock):
    name = blocks.CharBlock(required=False)
    page = PageChooserBlock(required=False)
    link = blocks.URLBlock(required=False)
    button = blocks.BooleanBlock(required=False)
    alignment = ChoiceBlock(
        choices=[
            ('left', _('Left')),
            ('center', _('Center')),
            ('right', _('Right')),
        ],
        required=False,
    )

    def __init__(self, required=True, local_blocks=None, **kwargs):
        super().__init__(local_blocks=local_blocks, **kwargs)
        self._required = required

    @property
    def required(self):
        return self._required

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        page = value.get('page')
        link = value.get('link')
        context.update({
            'href': page.url if page else link,
            'external': not bool(page),
            'text': value.get('name') or _('read more'),
            'align': value.get('alignment'),
            'button': value.get('button'),
        })
        return context

    def clean(self, value):
        at_lest_one_field_required_fields = ['page', 'link']
        if self.required and not any([bool(value.get(field)) for field in at_lest_one_field_required_fields]):
            error_message = _('At lest one of {} is required').format(at_lest_one_field_required_fields)
            errors = {field: ErrorList([error_message]) for field in at_lest_one_field_required_fields}
            raise ValidationError(error_message, params=errors)
        return super().clean(value)

    class Meta:
        icon = 'link'
        label = _('Read more')
        template = 'widgets/read-more-link.html'
        help_text = _('Choose either a page or an external link')


LINK_BLOCKS = [
    ('document', DocumentBlock()),
    ('read_more', ReadMoreBlock()),
]

BASE_BLOCKS += LINK_BLOCKS


class TeaserImageBlock(StructBlock):
    image = ImageChooserBlock(
        required=False, help_text='Recommended minimal width: 737px')
    position = ChoiceBlock(
        choices=[
            ('top', _('Top')),
            ('left', _('Left')),
            ('right', _('Right')),
        ],
        required=False,
    )
    large = BooleanBlock(required=False)


class TeaserBlock(StructBlock):
    title = blocks.CharBlock(required=False)
    content = RichTextBlock(required=False)
    image = TeaserImageBlock(required=False)
    page = PageChooserBlock(required=False)
    link = blocks.URLBlock(required=False)
    read_more_text = blocks.CharBlock(required=False)
    boarderless = blocks.BooleanBlock(required=False)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        page = value.get('page')
        link = value.get('link')
        image_block = value.get('image')
        image = image_block.get('image')
        imagepos = image_block.get('position')
        largeimg = image_block.get('large')
        read_more_text = value.get('read_more_text') or _('read more')
        lines = not value.get('boarderless')
        context.update({
            'href': page.url if page else link,
            'external': not bool(page),
            'title': value.get('title'),
            'description': value.get('content'),
            'readmorelink': {'text': read_more_text},
            'imgsrc': image.get_rendition('max-1200x1200').url if image else '',
            'imgpos': imagepos,
            'largeimg': largeimg,
            'lines': lines,
        })
        return context

    class Meta:
        icon = 'link'
        label = _('Teaser')
        template = 'widgets/teaser.html'
        help_text = _('Choose either a page or an external link')


class OverlayTeaserBlock(StructBlock):
    title = blocks.CharBlock()
    content = RichTextBlock(required=False)
    image = ImageChooserBlock(
        required=True, help_text='Recommended minimal width: 737px')
    page = PageChooserBlock(required=False)
    link = blocks.URLBlock(required=False)
    link_text = blocks.CharBlock(required=False)
    top_box = blocks.BooleanBlock(required=False, default=False)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        page = value.get('page')
        link = value.get('link')
        image = value.get('image')
        link_text = value.get('link_text') or _('link')
        top = value.get('top_box')
        context.update({
            'title': value.get('title'),
            'description': value.get('content'),
            'style': 'box',
            'links': [
                {
                    'href': page.url if page else link,
                    'text': link_text,
                    'external': not bool(page),
                },
            ],
            'imgsrc': image.get_rendition('max-1200x1200').url if image else '',
            'flapmd': True,
            'topposition': top,
        })
        return context

    class Meta:
        icon = 'link'
        label = _('Large Image Teaser')
        template = 'widgets/overlay-teaser-widgetchooser.html'
        help_text = _('Choose either a page or an external link')


class OverlayTeaserMapBlock(StructBlock):
    title = blocks.CharBlock()
    content = RichTextBlock(required=False)
    page = PageChooserBlock(required=False)
    link = blocks.URLBlock(required=False)
    link_text = blocks.CharBlock(required=False)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        page = value.get('page')
        link = value.get('link')
        link_text = value.get('link_text') or _('link')
        from wocat.cms.models import CountryPage
        country_pages = CountryPage.objects.live().in_menu()
        countries = [{'iso_3166_1_alpha_3': country_page.country.code} for country_page in country_pages]

        context.update({
            'title': value.get('title'),
            'description': value.get('content'),
            'style': 'box',
            'links': [
                {
                    'href': page.url if page else link,
                    'text': link_text,
                    'external': not bool(page),
                },
            ],
            'countries': countries,
            'size': 'large',
        })
        return context

    class Meta:
        icon = 'link'
        label = _('Map Teaser')
        template = 'widgets/overlay-teaser-widgetchooser.html'
        help_text = _('Choose either a page or an external link')


class TocBlock(StructBlock):
    title = blocks.CharBlock(default=_('Table of contents'), required=False)

    class Meta:
        icon = 'fa fa-list'
        label = _('Table of contents')
        template = 'cms/toc.html'

    #def render_form(self, value, prefix='', errors=None):
    #    form = super().render_form(value, prefix, errors)
    #    return format_html('<strong>{title}</b> {form}', title=_('Table of contents'), form=form)

    def get_content(self, context):
        page = context.get('page')
        if page and hasattr(page, 'content'):
            return page.content

    def get_headings(self, stream_content):
        headings = []
        for block in stream_content:
            if block.block_type == 'heading':
                headings.append({
                    'text': block.value,
                    'href': '#heading-{0}'.format(slugify(block.value))
                })
            elif block.block_type in ('columns_1_to_1', 'columns_1_to_2', 'columns_2_to_1'):
                headings.extend(self.get_headings(block.value.get('left_column')))
                headings.extend(self.get_headings(block.value.get('right_column')))
            elif block.block_type == 'columns_1_to_1_to_1':
                headings.extend(self.get_headings(block.value.get('left_column')))
                headings.extend(self.get_headings(block.value.get('middle_column')))
                headings.extend(self.get_headings(block.value.get('right_column')))
        return headings

    def render(self, value, context=None):
        if context:
            stream_content = self.get_content(context)
            if stream_content:
                context['headings'] = self.get_headings(stream_content)
                context['title'] = value.get('title')
        return super().render(value, context)


TOCBLOCKS = [
    ('toc', TocBlock()),
]


class DsfTocBlock(TocBlock):
    def get_content(self, context):
        section = context.get('section')
        if section:
            return section.get('content')


class DSFTeaserBlock(StructBlock):
    page = PageChooserBlock(required=False)
    module_1 = blocks.BooleanBlock(required=False, default=True)
    module_2 = blocks.BooleanBlock(required=False, default=True)
    module_3 = blocks.BooleanBlock(required=False, default=True)
    module_4 = blocks.BooleanBlock(required=False, default=True)
    module_5 = blocks.BooleanBlock(required=False, default=True)
    module_6 = blocks.BooleanBlock(required=False, default=True)
    module_7 = blocks.BooleanBlock(required=False, default=True)
    phase_b = blocks.BooleanBlock(required=False, default=True)
    phase_c = blocks.BooleanBlock(required=False, default=True)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        page = value.get('page')
        url = page.url if page else ''

        module_1 = value.get('module_1')
        module_2 = value.get('module_2')
        module_3 = value.get('module_3')
        module_4 = value.get('module_4')
        module_5 = value.get('module_5')
        module_6 = value.get('module_6')
        module_7 = value.get('module_7')

        context.update({
            'module1href': '{0}#module-1'.format(url) if module_1 else '',
            'module2href': '{0}#module-2'.format(url) if module_2 else '',
            'module3href': '{0}#module-3'.format(url) if module_3 else '',
            'module4href': '{0}#module-4'.format(url) if module_4 else '',
            'module5href': '{0}#module-5'.format(url) if module_5 else '',
            'module6href': '{0}#module-6'.format(url) if module_6 else '',
            'module7href': '{0}#module-7'.format(url) if module_7 else '',
        })
        return context

    class Meta:
        icon = 'link'
        label = _('DSF Teaser')
        template = 'widgets/dsf-teaser.html'


class UploadBlock(StructBlock):
    upload_slug = CharBlock(required=True)
    documents = ListBlock(DocumentBlock(required=False))

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        documents = value.get('documents')
        if documents:
            context.update({
                'context': '/static/styleguide/js/dropzone-endpoint.html',
            })
        return context

    def render(self, value, context=None):
        # Add the apiurl using the page id of the current page.
        if context:
            page = context.get('page')
            if page:
                section = context['section']
                if section:
                    module_id = section.get('module_id')
                    upload_slug = slugify(value.get('upload_slug'))
                    if module_id:
                        apiurl = reverse('cms:upload',
                                         kwargs={'page_pk': page.id, 'module_id': module_id,
                                                 'upload_slug': upload_slug})
                        context['apiurl'] = apiurl
            context['documents'] = self.child_blocks['documents'].render(value.get('documents'), context),
        return super().render(value, context)

    class Meta:
        icon = 'fa fa-upload'
        label = _('Upload')
        template = 'widgets/upload.html'


DSF_BLOCKS = BASE_BLOCKS + [('upload', UploadBlock())]
DSF_BLOCKS = DSF_BLOCKS + [('dsf_toc', DsfTocBlock())]


class DSFModulesBlock(StructBlock):
    module_1_title = CharBlock()
    module_1 = StreamBlock(DSF_BLOCKS)
    module_2_title = CharBlock()
    module_2 = StreamBlock(DSF_BLOCKS)
    module_3_title = CharBlock()
    module_3 = StreamBlock(DSF_BLOCKS)
    module_4_title = CharBlock()
    module_4 = StreamBlock(DSF_BLOCKS)
    module_5_title = CharBlock()
    module_5 = StreamBlock(DSF_BLOCKS)
    module_6_title = CharBlock()
    module_6 = StreamBlock(DSF_BLOCKS)
    module_7_title = CharBlock()
    module_7 = StreamBlock(DSF_BLOCKS)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        modules = {
            1: {'content': value.get('module_1'), 'color': '#403D38', 'text': value.get('module_1_title')},  # _('Operational Strategy and Action plan')
            2: {'content': value.get('module_2'), 'color': '#6E3237', 'text': value.get('module_2_title')},  # _('National and Subnational Level')
            3: {'content': value.get('module_3'), 'color': '#604F3B', 'text': value.get('module_3_title')},  # _('Landscape Level')}
            4: {'content': value.get('module_4'), 'color': '#3B482E', 'text': value.get('module_4_title')},  # _('Sea Level')
            5: {'content': value.get('module_5'), 'color': '#22454E', 'text': value.get('module_5_title')},  # _('SLM Territorial Planning')
            6: {'content': value.get('module_6'), 'color': '#2D446B', 'text': value.get('module_6_title')},  # _('Implementation and scaling out')
            7: {'content': value.get('module_7'), 'color': '#3A3451', 'text': value.get('module_7_title')},  # _('Knowledge management platform for informed decision making')
        }

        sections = []
        sidebar_links = []
        for i in range(1, 8):
            module = modules.get(i)
            content = module.get('content')
            if not content: continue  # Do not add this section if there is no content.
            sections.append({
                'content': module.get('content'),
                'id': 'module-{0}'.format(i),
                'module_id': i,
            })
            sidebar_links.append({
                'anchorlink': True,
                'color': 'white',
                'backgroundcolor': module.get('color'),
                'href': '#module-{0}'.format(i),
                'kicker': 'Module {0}'.format(i),
                'text': module.get('text'),
            })
        context.update({
            'sections': sections,
            'sidebar_links': sidebar_links,
            'context': context,
        })
        return context

    class Meta:
        icon = 'fa fa-th-list'
        label = _('DSF Modules')
        template = 'widgets/tab-infobox.html'


TEASER_BLOCKS = [
    ('teaser', TeaserBlock()),
    ('overlay_teaser', OverlayTeaserBlock()),
    ('media_teaser', MediaTeaserBlock()),
    ('news_teaser', NewsTeaserBlock()),
    ('user_teaser', UserTeaserBlock()),
    ('dsf_teaser', DSFTeaserBlock()),
    ('dsf_modules', DSFModulesBlock()),
]

BASE_BLOCKS += TEASER_BLOCKS

class MapBlock(StructBlock):
    class Meta:
        label = 'Map'
        template = 'map/map.html'
        icon = 'fa fa-map'


MAP_BLOCKS = [
    ('map', MapBlock())
]

BASE_BLOCKS += MAP_BLOCKS


class ImageGalleryElementBlock(StructBlock):
    image = ImageChooserBlock(help_text='Recommended minimal width: 737px')
    page = PageChooserBlock(required=False)
    link = blocks.URLBlock(required=False)
    description = blocks.CharBlock(required=False)
    shrink = ChoiceBlock(
        choices=[
            (1, _('S')),
            (2, _('XS')),
            (3, _('XXS')),
        ],
        required=False,
    )


class ImageGalleryBlock(StructBlock):
    columns = ChoiceBlock(
        choices=[
            (6, '2'),
            (4, '3'),
            (3, '4'),
        ],
        required=True,
    )
    elements = ListBlock(ImageGalleryElementBlock())
    vertical_align = blocks.BooleanBlock(required=False)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        columns = value.get('columns')
        vertical_align = value.get('vertical_align')
        elements = []
        for element in value.get('elements'):
            description = element.get('description')
            link = element.get('link')
            page = element.get('page')
            url = page.url if page else link
            image = element.get('image')
            image_url = image.get_rendition('max-1200x1200').url if image else ''
            shrink = element.get('shrink')
            if shrink:
                shrink = int(shrink)
            elements.append(
                {
                    'description': description,
                    'href': url,
                    'src': image_url,
                    'shrink': shrink,
                }
            )
        context['cols'] = columns
        context['images'] = elements
        context['verticalalign'] = vertical_align
        return context

    class Meta:
        icon = 'image'
        label = _('Image Gallery')
        template = 'widgets/image-gallery.html'


GALLERY_BLOCKS = [
    ('image_gallery', ImageGalleryBlock()),
]
BASE_BLOCKS += GALLERY_BLOCKS

BASE_BLOCKS += TOCBLOCKS


class SubpagesBlock(StructBlock):
    class Meta:
        icon = 'fa fa-bars'
        label = 'Subpages'
        template = 'cms/page-listing.html'

    def render_form(self, value, prefix='', errors=None):
        form = super().render_form(value, prefix, errors)
        return format_html('<strong>{title}</b> {form}', title=_('Subpages'), form=form)

    def render(self, value, context=None):
        if context:
            page = context['page']
            context['pages'] = page.get_children().live().in_menu()
            context['title'] = _('Subpages')
        return super().render(value, context)


SUBPAGEBLOCKS = [
    ('subpages', SubpagesBlock()),
]

BASE_BLOCKS += SUBPAGEBLOCKS


class ColumnsBlock(StructBlock):
    left_column = StreamBlock(BASE_BLOCKS + CONTACT_PERSON_TEASER_BLOCKS)
    right_column = StreamBlock(BASE_BLOCKS + CONTACT_PERSON_TEASER_BLOCKS)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        context['left_column'] = value.get('left_column')
        context['right_column'] = value.get('right_column')
        return context

    class Meta:
        icon = 'fa fa-columns'
        label = 'Columns 1-1'
        template = None


class Columns1To1Block(ColumnsBlock):
    class Meta:
        label = 'Columns 1:1'
        template = 'widgets/columns-1-1.html'


class Columns1To2Block(ColumnsBlock):
    class Meta:
        label = 'Columns 1:2'
        template = 'widgets/columns-1-2.html'


class Columns2To1Block(ColumnsBlock):
    class Meta:
        label = 'Columns 2:1'
        template = 'widgets/columns-2-1.html'


class Columns1To1To1Block(ColumnsBlock):
    middle_column = StreamBlock(BASE_BLOCKS + CONTACT_PERSON_TEASER_BLOCKS)

    class Meta:
        label = 'Columns 1:1:1'
        template = 'widgets/columns-1-1-1.html'

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        context['middle_column'] = value.get('middle_column')
        return context


COLUMNS_BLOCKS = [
    ('columns_1_to_1', Columns1To1Block()),
    ('columns_1_to_2', Columns1To2Block()),
    ('columns_2_to_1', Columns2To1Block()),
    ('columns_1_to_1_to_1', Columns1To1To1Block()),
]

CMS_BLOCKS = BASE_BLOCKS + MAP_BLOCKS + TEASER_BLOCKS + COLUMNS_BLOCKS

IMAGE_BLOCKS = [
    ('image', ImageBlock(
        help_text='Recommended minimal resolution: 1800px x 600px')),
]

# CAROUSEL_BLOCKS = (
#     ('image', ImageBlock()),
#     # ('carousel', CarouselBlock()),
# )
# HEADER_BLOCKS = CAROUSEL_BLOCKS

EXTRA_BLOCKS = COLUMNS_BLOCKS + [
    ('html', RawHTMLBlock()),
]

ALL_BLOCKS = CMS_BLOCKS + EXTRA_BLOCKS


PROJECT_BLOCKS = CMS_BLOCKS + CONTACT_PERSON_TEASER_BLOCKS
COUNTRY_BLOCKS = PROJECT_BLOCKS
REGION_BLOCKS = PROJECT_BLOCKS
EVENTS_BLOCKS = PROJECT_BLOCKS
