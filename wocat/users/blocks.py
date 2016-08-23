from django.forms import Select
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _
from django.utils.html import format_html
from wagtail.wagtailcore.blocks import StructBlock, ChooserBlock


class UserChooserBlock(ChooserBlock):
    widget = Select

    @cached_property
    def target_model(self):
        from .models import User
        return User

    # Return the key value for the select field
    def value_for_form(self, value):
        if isinstance(value, self.target_model):
            return value.pk
        else:
            return value


class UserTeaserBlock(StructBlock):
    user = UserChooserBlock(required=True)

    def get_context(self, value):
        user = value.get('user')
        if not user:
            return {}
        return {
            'title': user.name,
            'description': format_html(
                '<p>{institution}<br>{position}<br>{email}</p>',
                institution=user.institution,
                position=user.position,
                email=user.email_safe,
            ),
            'href': user.get_absolute_url(),
            'readmorelink': {'text': _('view profile')},
            'imgpos': 'left',
            'imgsrc': user.avatar.url if user.avatar else '',
        }

    class Meta:
        icon = 'fa fa-user'
        label = _('Member Teaser')
        template = 'widgets/teaser.html'


USER_TEASER_BLOCKS = [
    ('user_teaser', UserTeaserBlock()),
]
