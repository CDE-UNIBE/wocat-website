from classytags.helpers import InclusionTag
from django import template
from django.utils.translation import ugettext_lazy as _

register = template.Library()


@register.tag
class MediaWidget(InclusionTag):
    name = 'mediateaser'
    template = 'widgets/teaser.html'

    def get_context(self, context, **kwargs):
        media = context.get('media')
        if media:
            title = media.title
            abstract = media.abstract
            media_type = media.media_type
            video = media.video
            file = media.file
            teaser_image = media.image.get_rendition('max-1200x1200').url if media.image else ''
            author = media.author
            countries = media.countries
            image_position = 'top'
            content = media.content
            url = media.get_absolute_url()
            if not content and file:
                href = file.url
                readmorelink = _('Download')
            else:
                href = url
                readmorelink = _('Show media')
            return {
                'href': href,
                'title': title,
                'description': abstract,
                'author': media.author,
                'readmorelink': {'text': readmorelink},
                'imgsrc': teaser_image,
                'imgpos': image_position or 'top',
                'mediastyle': True,
            }
        else:
            return {}
