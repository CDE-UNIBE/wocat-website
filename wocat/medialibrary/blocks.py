from django.forms import Select
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.blocks import StructBlock, ChoiceBlock
from django.utils.translation import ugettext_lazy as _
from django.utils.functional import cached_property


class MediaChooserBlock(blocks.ChooserBlock):
    widget = Select

    @cached_property
    def target_model(self):
        from .models import Media
        return Media

    # Return the key value for the select field
    def value_for_form(self, value):
        if isinstance(value, self.target_model):
            return value.pk
        else:
            return value


class MediaTeaserBlock(StructBlock):
    media = MediaChooserBlock(required=True)
    image_position = ChoiceBlock(
        choices=[
            ('top', 'Top'),
            ('left', 'Left'),
            ('right', 'Right'),
        ],
        required=False,
    )

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        media = value.get('media')
        title = media.title
        abstract = media.abstract
        media_type = media.media_type
        video = media.video
        file = media.file
        teaser_image = media.teaser_image.get_rendition('max-1200x1200').url if media.teaser_image else ''
        author = media.author
        year = media.year
        languages = [language.name for language in media.languages.all()]
        country = media.countries
        image_position = value.get('image_position')
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

    class Meta:
        icon = 'fa fa-file'
        label = 'Media Teaser'
        template = 'widgets/teaser.html'
