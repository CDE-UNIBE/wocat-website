from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.blocks import RawHTMLBlock, StructBlock, PageChooserBlock, BooleanBlock, ChoiceBlock, \
    StreamBlock
from wagtail.wagtailembeds.blocks import EmbedBlock as WagtailEmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock

from django.utils.translation import ugettext_lazy as _


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


class OptionalExternalLinkBlock(StructBlock):
    text = blocks.CharBlock(required=False)
    url = blocks.URLBlock(required=False)


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
    content = blocks.RichTextBlock(required=False)
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

ALL_BLOCKS = COLUMNS_BLOCKS + [
    ('html', RawHTMLBlock()),
]
