from classytags.helpers import InclusionTag
from django import template
from django.utils.translation import ugettext_lazy as _

register = template.Library()


@register.tag
class News(InclusionTag):
    name = 'news'
    template = 'widgets/teaser.html'

    def get_context(self, context, **kwargs):
        news = context.get('news')
        if not news:
            return {}

        news_context = {
            'title': news.title,
            'description': news.lead,
            'author': news.author,
            'date': news.date,
            'href': news.url,
            'readmorelink': {'text': _('read more')},
            # 'bottomline': True,
        }

        if news.lead_image:
            news_context.update({
                'imgpos': 'right',
                'imgsrc': news.lead_image.get_rendition('max-500x500').url,
            })

        return news_context
