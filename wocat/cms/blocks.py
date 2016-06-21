from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.blocks import RawHTMLBlock, StructBlock, PageChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock as WagtailEmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock


class HeadingBlock(blocks.CharBlock):
    class Meta:
        classname = 'full title'
        icon = 'title'
        template = 'widgets/heading.html'

    def get_context(self, value):
        context = super().get_context(value)
        context['level'] = 1
        context['content'] = value
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
        context['url'] = value.get_rendition('max-1200x1200').url
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


class TeaserBlock(StructBlock):
    title = blocks.CharBlock()
    content = blocks.RichTextBlock()
    page = PageChooserBlock(required=False)
    external_link = blocks.URLBlock(required=False)

    def get_context(self, value):
        context = super().get_context(value)

        title = value.get('title')
        context['title'] = title

        content = value.get('content')
        context['content'] = content

        page = value.get('page')
        external_link = value.get('external_link')
        if page:
            link = {
                'text': page.title,
                'url': page.url,
            }
            external = False
        elif external_link:
            link = external_link
            external = True
        else:
            link = ''
            external = False
        context['link'] = link
        context['external'] = external
        return context

    class Meta:
        icon = 'fa fa-link'
        label = 'Link'
        template = 'widgets/read-more-link.html'
        help_text = 'Choose either a page or an external link'

# class LinkBlock(StructBlock):
#     title = CharBlock(required=True)
#     picture = ImageChooserBlock(required=False)
#     text = RichTextBlock(required=False)
#     link = URLBlock(required=False)
#     date = DateBlock(required=False)
#
#     class Meta:
#         classname = 'link'
#         icon = 'fa fa-external-link'
#         template = 'widgets/page-teaser-wide.html'
#
#     def get_context(self, value):
#         context = super().get_context(value)
#         context['arrow_right_link'] = True
#         context['title'] = value.get('title')
#         context['description'] = value.get('text')
#         context['date'] = value.get('date')
#
#         image = value.get('picture')
#         if image:
#             rendition = image.get_rendition('fill-640x360-c100')
#             context['image'] = {'url': rendition.url, 'name': image.title}
#         if value.get('link'):
#             context['href'] = value.get('link')
#         return context

ALL_BLOCKS = BASE_BLOCKS + [
    ('html', RawHTMLBlock()),
]



# class QABlock(StructBlock):
#     question = CharBlock()
#     answer = RichTextBlock()
#
#
# class FAQBlock(StructBlock):
#     title = CharBlock()
#     faqs = ListBlock(QABlock())
#
#     class Meta:
#         icon = 'fa fa-medkit'
#         template = 'blocks/faq_block.html'
#
#     def get_context(self, value):
#         context = super().get_context(value)
#         context['titel'] = value.get('title')
#         context['list'] = []
#         for faq in value.get('faqs'):
#             res = {'term': faq.get('question'),
#                    'definitions': [{'text': faq.get('answer')}],
#                    'opened': False,
#                    'notoggle': False
#                    }
#             context['list'] += [res]
#         return context
