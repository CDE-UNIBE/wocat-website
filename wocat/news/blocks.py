from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailcore.blocks import PageChooserBlock, StructBlock


class NewsChooserBlock(PageChooserBlock):
    @cached_property
    def target_model(self):
        from wocat.news.models import NewsPage
        return NewsPage

    @cached_property
    def widget(self):
        from wagtail.wagtailadmin.widgets import AdminPageChooser
        return AdminPageChooser(target_models=[self.target_model], can_choose_root=self.can_choose_root)


class NewsTeaserBlock(StructBlock):
    news = NewsChooserBlock(required=True)

    def get_context(self, value):
        news = value.get('news')
        if not news:
            return {}

        context = {
            'title': news.title,
            'description': news.lead,
            'author': news.author,
            'date': news.date,
            'href': news.url,
            'readmorelink': {'text': _('read more')},
            'bottomline': True,
        }

        if news.lead_image:
            context.update({
                'imgpos': 'right',
                'imgsrc': news.lead_image.get_rendition('max-500x500').url,
            })

        return context

    class Meta:
        icon = 'fa fa-newspaper-o'
        label = _('News Teaser')
        template = 'widgets/teaser.html'


NEWS_TEASER_BLOCKS = [
    ('news_teaser', NewsTeaserBlock()),
]
