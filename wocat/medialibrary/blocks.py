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

    def value_from_form(self, value):
        # If no user was selected, value is an empty string which raises errors
        # when validating the form. In this case, return empty early.
        if value == '':
            return None
        return super().value_from_form(value)


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

    def get_context(self, value, parent_context=None):
        media = value.get('media')
        if not media:
            # Media can be deleted, there is no cascading to the teaser-object in case this happens.
            return {}

        teaser_image = media.teaser_image.get_rendition('max-1200x1200').url if media.teaser_image else ''
        author = media.author
        year = media.year
        languages = [language.name for language in media.languages.all()]
        image_position = value.get('image_position')

        if not media.content and media.file:
            href = media.file.url
            readmorelink = _('Download')
        else:
            href = media.get_absolute_url()
            readmorelink = _('Show media')
        return {
            'href': href,
            'title': media.title,
            'description': media.abstract,
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
        label = _('Media Teaser')
        template = 'widgets/teaser.html'
