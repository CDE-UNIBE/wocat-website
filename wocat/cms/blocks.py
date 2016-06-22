from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.blocks import RawHTMLBlock, StructBlock, PageChooserBlock, BooleanBlock, ChoiceBlock, \
    StreamBlock, ListBlock
from wagtail.wagtailembeds.blocks import EmbedBlock as WagtailEmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock

from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string


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

    @property
    def url(self):
        if self.page:
            return self.page.url
        elif self.link:
            return self.link

    @property
    def external(self):
        return not bool(self.page)

    def get_context(self, value):
        page = value.get('page')
        url = self.url
        return {
            'url': url,
            'external': self.external,
            'name': value.get('name'),
        }

    def clean(self, value):
        at_lest_one_field_required_fields = ['page', 'url']
        if self.required and not any([bool(value.get(field)) for field in at_lest_one_field_required_fields]):
            error_message = _('At lest one of {} is required').format(at_lest_one_field_required_fields)
            errors = {field: ErrorList([error_message]) for field in at_lest_one_field_required_fields}
            raise ValidationError(error_message, params=errors)
        return super().clean(value)


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

    def get_context(self, value):
        page = value.get('page')
        link = value.get('link')
        image_block = value.get('image')
        image = image_block.get('image')
        imagepos = image_block.get('position')
        largeimg = image_block.get('large')
        return {
            'href': page.url if page else link,
            'external': not bool(page),
            'title': value.get('title'),
            'description': value.get('content'),
            'readmorelink': {'text': 'read more'},
            'imgsrc': image.get_rendition('max-1200x1200').url if image else '',
            'imgpos': imagepos,
            'largeimg': largeimg,
            'lines': True,
        }

    class Meta:
        icon = 'link'
        label = _('Teaser')
        template = 'widgets/teaser.html'
        help_text = 'Choose either a page or an external link'


TEASER_BLOCKS = [
    ('teaser', TeaserBlock()),
]

BASE_BLOCKS += TEASER_BLOCKS


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

CORE_BLOCKS = BASE_BLOCKS + TEASER_BLOCKS + COLUMNS_BLOCKS


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
#         help_text = 'Choose either a page or an external link'

class CarouselSlideBlock(StructBlock):
    image = ImageBlock()
    name = blocks.CharBlock(required=False)
    content = RichTextBlock(required=False)
    link = LinkBlock(required=False)


class CarouselBlock(StructBlock):
    images = ListBlock(ImageBlock())
    heading = blocks.CharBlock()
    content = RichTextBlock(required=False)

    def get_context(self, value):
        images = value.get('images')
        heading = value.get('heading')
        content = value.get('content')
        print(images)
        return {
            'carousel': {
                'id': 1,
                'items': [{'src': image.get_rendition('max-1200x1200').url} for image in images],
            },
            'overlay': {
                'heading': heading,
                'lead': content,
            },
        }

    def render(self, value):
        carousel = render_to_string('widgets/carousel.html', context=self.get_context(value).get('carousel'))
        overlay = render_to_string('widgets/page-lead-overlay.html', context=self.get_context(value).get('overlay'))
        return carousel + overlay

    class Meta:
        icon = 'picture'
        label = _('Carousel')


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
#         help_text = 'Choose either a page or an external link'


CAROUSEL_BLOCKS = (
    ('carousel', CarouselBlock()),
)
HEADER_BLOCKS = CAROUSEL_BLOCKS

EXTRA_BLOCKS = COLUMNS_BLOCKS + [
    ('html', RawHTMLBlock()),
]

ALL_BLOCKS = CORE_BLOCKS + EXTRA_BLOCKS
