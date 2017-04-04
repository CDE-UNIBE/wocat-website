from django.contrib.auth.models import Group
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailcore import hooks


class NewsletterAdminMenuItem:
    order = 90000

    @staticmethod
    def render_html(request):
        output = '''<li class="menu-item">
                        <a href="{0}" class="fa fa-envelope-o" target="_blank">{1}</a>
                    </li>'''.format(reverse('newsletter:index'), _('Newsletter'))
        # </li>'''.format(reverse(''))
        return output


@hooks.register('construct_main_menu')
def main_menu_django_admin_item(request, menu_items):
    """
    Adding a newsletter management item to the cms menu.
    Checking permission to group "Newsletter Moderators".
    """
    user = request.user
    newsletter_group, created = Group.objects.get_or_create(name='Newsletter Moderators')
    if user and newsletter_group in user.groups.all():
        menu_items.append(NewsletterAdminMenuItem())
