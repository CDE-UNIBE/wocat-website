from django.core.exceptions import ValidationError
from django.forms import Select
from django.forms.utils import ErrorList
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.blocks import RawHTMLBlock, StructBlock, PageChooserBlock, BooleanBlock, ChoiceBlock, \
    StreamBlock, ListBlock
from wagtail.wagtailembeds.blocks import EmbedBlock as WagtailEmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock

from wocat.medialibrary.models import Media
from wocat.news.blocks import NewsTeaserBlock


class HeadingBlock(blocks.CharBlock):
    class Meta:
        classname = 'full title'
        icon = 'title'
        template = 'widgets/heading1.html'

    def get_context(self, value):
        context = super().get_context(value)
        context['text'] = value
        return context


class RichTextBlock(blocks.RichTextBlock):
    class Meta:
        icon = 'pilcrow'
        template = 'widgets/richtext.html'

    def get_context(self, value):
        context = super().get_context(value)
        context['content'] = value
        return context


class ImageBlock(ImageChooserBlock):
    class Meta:
        icon = 'image'
        template = 'widgets/image.html'

    def get_context(self, value):
        context = super().get_context(value)
        context['src'] = value.get_rendition('max-1200x1200').url
        context['name'] = value.title
        return context


class EmbedBlock(WagtailEmbedBlock):
    class Meta:
        icon = 'media'
        template = 'widgets/embed.html'

    def get_context(self, value):
        context = super().get_context(value)
        embed = value
        context['embed'] = embed
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

    def get_context(self, value):
        page = value.get('page')
        link = value.get('link')
        return {
            'href': page.url if page else link,
            'external': not bool(page),
            'text': value.get('name') or _('read more'),
        }

    def clean(self, value):
        at_lest_one_field_required_fields = ['page', 'url']
        if self.required and not any([bool(value.get(field)) for field in at_lest_one_field_required_fields]):
            error_message = _('At lest one of {} is required').format(at_lest_one_field_required_fields)
            errors = {field: ErrorList([error_message]) for field in at_lest_one_field_required_fields}
            raise ValidationError(error_message, params=errors)
        return super().clean(value)


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

    def __init__(self, required=True, local_blocks=None, *args, **kwargs):
        super().__init__(local_blocks=local_blocks, *args, **kwargs)
        self.required = required

    def get_context(self, value):
        page = value.get('page')
        link = value.get('link')
        return {
            'href': page.url if page else link,
            'external': not bool(page),
            'text': value.get('name') or _('read more'),
            'align': value.get('alignment'),
            'button': value.get('button'),
        }

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
    ('read_more', ReadMoreBlock()),
]

BASE_BLOCKS += LINK_BLOCKS


class TeaserImageBlock(StructBlock):
    image = ImageChooserBlock(required=False)
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
    title = blocks.CharBlock()
    content = RichTextBlock(required=False)
    image = TeaserImageBlock(required=False)
    page = PageChooserBlock(required=False)
    link = blocks.URLBlock(required=False)
    read_more_text = blocks.CharBlock(required=False)

    def get_context(self, value):
        page = value.get('page')
        link = value.get('link')
        image_block = value.get('image')
        image = image_block.get('image')
        imagepos = image_block.get('position')
        largeimg = image_block.get('large')
        read_more_text = value.get('read_more_text') or _('read more')
        return {
            'href': page.url if page else link,
            'external': not bool(page),
            'title': value.get('title'),
            'description': value.get('content'),
            'readmorelink': {'text': read_more_text},
            'imgsrc': image.get_rendition('max-1200x1200').url if image else '',
            'imgpos': imagepos,
            'largeimg': largeimg,
            'lines': True,
        }

    class Meta:
        icon = 'link'
        label = _('Teaser')
        template = 'widgets/teaser.html'
        help_text = _('Choose either a page or an external link')


class MediaChooserBlock(blocks.ChooserBlock):
    target_model = Media
    widget = Select

    # Return the key value for the select field
    def value_for_form(self, value):
        if isinstance(value, self.target_model):
            return value.pk
        else:
            return value


class MediaTeaserBlock(StructBlock):
    media = MediaChooserBlock(required=True)

    def get_context(self, value):
        media = value.get('media')
        page = media.detail_page
        file = media.file
        return {
            'href': page.url if page else file.url,
            'title': media.title,
            'description': format_html(
                '{description}<p>{author_label}: {author}</p>',
                description=media.description,
                author_label=_('Author'),
                author=media.author
            ),
            'readmorelink': {'text': _('Detail page') if page else _('Download')},
            'imgsrc': media.teaser_image.get_rendition('max-1200x1200').url if media.teaser_image else '',
            'imgpos': 'left',
        }

    class Meta:
        icon = 'fa fa-file-o'
        label = _('Media Teaser')
        template = 'widgets/teaser.html'


TEASER_BLOCKS = [
    ('teaser', TeaserBlock()),
    ('media_teaser', MediaTeaserBlock()),
    ('news_teaser', NewsTeaserBlock()),
]

BASE_BLOCKS += TEASER_BLOCKS


class ImageGalleryElementBlock(StructBlock):
    image = ImageChooserBlock()
    page = PageChooserBlock(required=False)
    link = blocks.URLBlock(required=False)
    description = blocks.CharBlock(required=False)
    shrink = ChoiceBlock(
        choices=[
            (1, _('Small')),
            (2, _('Extra small')),
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

    def get_context(self, value):
        context = super().get_context(value)
        columns = value.get('columns')
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
        return context

    class Meta:
        icon = 'image'
        label = _('Image Gallery')
        template = 'widgets/image-gallery.html'


GALLERY_BLOCKS = [
    ('image_gallery', ImageGalleryBlock()),
]
BASE_BLOCKS += GALLERY_BLOCKS


class ColumnsBlock(StructBlock):
    left_column = StreamBlock(BASE_BLOCKS)
    right_column = StreamBlock(BASE_BLOCKS)

    def get_context(self, value):
        context = super().get_context(value)
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
    middle_column = StreamBlock(BASE_BLOCKS)

    class Meta:
        label = 'Columns 1:1:1'
        template = 'widgets/columns-1-1-1.html'

    def get_context(self, value):
        context = super().get_context(value)
        context['middle_column'] = value.get('middle_column')
        return context


COLUMNS_BLOCKS = [
    ('columns_1_to_1', Columns1To1Block()),
    ('columns_1_to_2', Columns1To2Block()),
    ('columns_2_to_1', Columns2To1Block()),
    ('columns_1_to_1_to_1', Columns1To1To1Block()),
]

CMS_BLOCKS = BASE_BLOCKS + TEASER_BLOCKS + COLUMNS_BLOCKS

# class CarouselBlock(StructBlock):
#     title = blocks.CharBlock()
#     content = RichTextBlock(required=False)
#     images = ListBlock(ImageBlock())
#     link = OptionalLinkBlock()
#
#     def get_context(self, value):
#         page = value.get('page')
#         link = value.get('link')
#         images = value.get('images')
#         return {
#             'id': 1,
#             'external': not bool(page),
#             'title': value.get('title'),
#             'description': value.get('content'),
#             'readmorelink': {'text': 'read more'},
#             'imgsrc': image.get_rendition('max-1200x1200').url if image else '',
#             'imgpos': imagepos,
#             'largeimg': largeimg,
#             'lines': True,
#         }
#
#     class Meta:
#         icon = 'link'
#         label = _('Teaser')
#         template = 'widgets/teaser.html'
#         help_text = _('Choose either a page or an external link')

# class CarouselSlideBlock(StructBlock):
#     image = ImageBlock()
#     name = blocks.CharBlock(required=False)
#     content = RichTextBlock(required=False)
#     link = LinkBlock(required=False)


# class CarouselBlock(ListBlock(ImageBlock)):
#
#     def get_context(self, value):
#         images = value.get('images')
#         heading = value.get('heading')
#         content = value.get('content')
#         return {
#             'carousel': {
#                 'id': 1,
#                 'items': [{'src': image.get_rendition('max-1200x1200').url} for image in images],
#             },
#             'overlay': {
#                 'heading': heading,
#                 'lead': content,
#             },
#         }
#
#     def render(self, value):
#         carousel = render_to_string('widgets/carousel.html', context=self.get_context(value).get('carousel'))
#         overlay = render_to_string('widgets/page-lead-overlay.html', context=self.get_context(value).get('overlay'))
#         return carousel + overlay
#
#     class Meta:
#         icon = 'picture'
#         label = _('Carousel')


# class CarouselBlock(StructBlock):
#     images = ListBlock(ImageBlock())
#     heading = blocks.CharBlock()
#     content = RichTextBlock(required=False)
#
#     def get_context(self, value):
#         images = value.get('images')
#         heading = value.get('heading')
#         content = value.get('content')
#         return {
#             'carousel': {
#                 'id': 1,
#                 'items': [{'src': image.get_rendition('max-1200x1200').url} for image in images],
#             },
#             'overlay': {
#                 'heading': heading,
#                 'lead': content,
#             },
#         }
#
#     def render(self, value):
#         carousel = render_to_string('widgets/carousel.html', context=self.get_context(value).get('carousel'))
#         overlay = render_to_string('widgets/page-lead-overlay.html', context=self.get_context(value).get('overlay'))
#         return carousel + overlay
#
#     class Meta:
#         icon = 'picture'
#         label = _('Carousel')


# class CarouselHeadingBlock(StructBlock):
#     images = ListBlock(ImageBlock())
#     heading = blocks.CharBlock()
#     content = RichTextBlock(required=False)
#
#     def get_context(self, value):
#         images = value.get('images')
#         heading = value.get('heading')
#         content = value.get('content')
#         return {
#             'carousel': {
#                 'id': 1,
#                 'items': [{'src': image.get_rendition('max-1200x1200').url} for image in images],
#             },
#             'overlay': {
#                 'heading': heading,
#                 'lead': content,
#             },
#         }
#
#     def render(self, value):
#         carousel = render_to_string('widgets/carousel.html', context=self.get_context(value).get('carousel'))
#         overlay = render_to_string('widgets/page-lead-overlay.html', context=self.get_context(value).get('overlay'))
#         return carousel + overlay
#
#     class Meta:
#         icon = 'picture'
#         label = _('Carousel')
#
#
# class CarouselTeaserBlock(StructBlock):
#     images = ListBlock(CarouselSlideBlock())
#     name = blocks.CharBlock(required=False)
#     content = RichTextBlock(required=False)
#     link = LinkBlock(required=False)
#
#     def get_context(self, value):
#         page = value.get('page')
#         link = value.get('link')
#         images = value.get('images')
#         return {
#             'id': 1,
#             'external': not bool(page),
#             'title': value.get('title'),
#             'description': value.get('content'),
#             'readmorelink': {'text': 'read more'},
#             'imgsrc': image.get_rendition('max-1200x1200').url if image else '',
#             'imgpos': imagepos,
#             'largeimg': largeimg,
#             'lines': True,
#         }
#
#     class Meta:
#         icon = 'link'
#         label = _('Teaser')
#         template = 'widgets/teaser.html'
#         help_text = _('Choose either a page or an external link')


IMAGE_BLOCKS = [
    ('image', ImageBlock()),
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
