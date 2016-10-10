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
            ('top', _('Top')),
            ('left', _('Left')),
            ('right', _('Right')),
        ],
        required=False,
    )

    def get_context(self, value):
        context = {}
        media = value.get('media')
        title = media.title
        abstract = media.abstract
        media_type = media.media_type
        video = media.video
        file = media.file
        teaser_image = media.teaser_image.get_rendition('max-1200x1200').url if media.teaser_image else ''
        author = media.author
        country = media.country
        image_position = value.get('image_position')
        content = media.content
        url = media.get_absolute_url()
        return {
            'href': file.url if file else url,
            'title': title,
            'description': abstract,
            'author': media.author,
            'readmorelink': {'text': _('Show media') if content else _('Download')},
            'imgsrc': teaser_image,
            'imgpos': image_position or 'top',
            'mediastyle': True,
        }

    class Meta:
        icon = 'fa fa-file'
        label = _('Media Teaser')
        template = 'widgets/teaser.html'
