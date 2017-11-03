from classytags.helpers import InclusionTag
from django import template
from django.template.defaultfilters import truncatewords
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
            year = media.year
            languages = [language.name for language in media.languages.all()]
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
                'author': '{author}{year}{languages}'.format(
                    author='Author: {0}'.format(author) if author else '',
                    year='{0}Year: {1}'.format(', ' if author else '', year) if year else '',
                    languages='{0}Languages: {1}'.format(', ' if author or year else '',
                                                         ', '.join(languages)) if languages else ''
                ),
                'readmorelink': {'text': readmorelink},
                'imgsrc': teaser_image,
                'imgpos': image_position or 'top',
                'mediastyle': True,
            }
        else:
            return {}


@register.tag
class MediaGalleryWidget(MediaWidget):
    """
    Basically the MediaWidget but with "image_placeholder" passed to the
    context. Used to display placeholders for media without preview images.
    """
    name = 'mediagallery'
    template = 'widgets/media-gallery-item.html'

    def get_context(self, context, **kwargs):
        context = super().get_context(context, **kwargs)

        if context.get('description'):
            context['description'] = truncatewords(context['description'], 20)

        return context
