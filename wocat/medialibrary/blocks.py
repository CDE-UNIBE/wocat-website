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
        media = value.get('media')
        page = media.detail_page
        file = media.file
        image_position = value.get('image_position')
        return {
            'href': page.url if page else file.url,
            'title': media.title,
            'description': media.description,
            'author': media.author,
            'readmorelink': {'text': _('Detail page') if page else _('Download')},
            'imgsrc': media.teaser_image.get_rendition('max-1200x1200').url if media.teaser_image else '',
            'imgpos': image_position or 'top',
            'mediastyle': True,
        }

    class Meta:
        icon = 'fa fa-file-o'
        label = _('Media Teaser')
        template = 'widgets/teaser.html'
