from django.forms import Select
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _
from django.utils.html import format_html
from wagtail.wagtailcore.blocks import StructBlock, ChooserBlock
#from wagtail.wagtailcore.blocks.base import accepts_context
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


class BlockWithContextMixin:
    def render(self, value, context=None):
        """
        Overwrite of Wagtail Block's default:
        Return a text rendering of 'value', suitable for display on templates. By default, this will
        use a template (with the passed context, supplemented by the result of get_context) if a
        'template' property is specified on the block, and fall back on render_basic otherwise.

        Alteration: Call get_context with context if it accepts it.
        """
        template = getattr(self.meta, 'template', None)
        if not template:
            return self._render_basic_with_context(value, context=context)

        if context is None:
            new_context = {}
        else:
            new_context = dict(context)

        #if accepts_context(self.get_context):
        new_context.update(self.get_context(value, new_context))
        #else:
        #    new_context.update(self.get_context(value))

        return mark_safe(render_to_string(template, new_context))


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

    def value_from_form(self, value):
        # If no user was selected, value is an empty string which raises errors
        # when validating the form. In this case, return empty early.
        if value == '':
            return None
        return super().value_from_form(value)


class UserTeaserBlock(StructBlock):
    user = UserChooserBlock(required=True)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        user = value.get('user')
        if not user:
            return context
        if user.country:
            flag = format_html('<img src="{src}" class="inlineflag" alt="{name}"> {name}',
                src=user.country.flag, name=user.country.name)
        else:
            flag = None
        context.update({
            'title': user.name,
            'description': format_html(
                '<p>{institution}{position}{email}{country}</p>',
                institution=user.institution or '',
                position=format_html('<br>{0}', user.position) if user.position else '',
                email=format_html('<br>{0}', user.email_safe) if user.email_safe else '',
                country=format_html('<br>{0}', flag) if flag else '',
            ),
            'href': user.get_absolute_url(),
            'readmorelink': {'text': _('View profile')},
            'imgpos': 'left',
            'imgsrc': user.avatar['avatarsquare'].url if user.avatar else '',
            'imgcircle': True,
        })
        return context

    class Meta:
        icon = 'fa fa-user'
        label = 'Member Teaser'
        template = 'widgets/teaser.html'


USER_TEASER_BLOCKS = [
    ('user_teaser', UserTeaserBlock()),
]


class SubpagesBlock(StructBlock):
    class Meta:
        icon = 'fa fa-bars'
        label = 'Subpages'
        template = 'cms/page-listing.html'

    def render_form(self, value, prefix='', errors=None):
        form = super().render_form(value, prefix, errors)
        return format_html('<strong>{title}</b> {form}', title='Subpages', form=form)


SUBPAGEBLOCKS = [
    ('subpages', SubpagesBlock()),
]


class ContactPersonTeaserBlock(BlockWithContextMixin, StructBlock):
    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        page = context.get('page')
        if page and hasattr(page, 'contact_person'):
            user = page.contact_person
        else:
            return context
        if user.country:
            flag = format_html('<img src="{src}" class="inlineflag" alt="{name}"> {name}',
                src=user.country.flag, name=user.country.name)
        else:
            flag = None
        context.update({
            'title': user.name,
            'description': format_html(
                '<p>{institution}{position}{email}{country}</p>',
                institution=user.institution or '',
                position=format_html('<br>{0}', user.position) if user.position else '',
                email=format_html('<br>{0}', user.email_safe) if user.email_safe else '',
                country=format_html('<br>{0}', flag) if flag else '',
            ),
            'href': user.get_absolute_url(),
            'readmorelink': {'text': _('View profile')},
            'imgpos': 'left',
            'imgsrc': user.avatar['avatarsquare'].url if user.avatar else '',
            'imgcircle': True,
        })
        return context

    #def render_form(self, value, prefix='', errors=None):
    #    form = super().render_form(value, prefix, errors)
    #    return format_html('<strong>{title}</b> {form}', title=_('Contact Person Teaser'), form=form)

    class Meta:
        icon = 'fa fa-user'
        label = 'Contact Person Teaser'
        template = 'widgets/teaser.html'


CONTACT_PERSON_TEASER_BLOCKS = [
    ('contact_person_teaser', ContactPersonTeaserBlock()),
]
