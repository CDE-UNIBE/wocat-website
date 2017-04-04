from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.views.generic import View
from django.views.generic import TemplateView

from .filters import UserFilter

User = get_user_model()


# API_KEY = settings.NEWSLETTER_API_KEY
# LIST_ID = settings.NEWSLETTER_LIST_ID
#
#
# def get_api():
#     if API_KEY and LIST_ID:
#         return mailchimp.Mailchimp(API_KEY)
#
#
# def subscribe_to_newsletter(user):
#     api = get_api()
#     if api and user:
#         api.lists.subscribe(LIST_ID, {'email': user.email}, update_existing=True)
#         return True
#     else:
#         return False
#
#
# def unsubscribe_from_newsletter(user):
#     api = get_api()
#     if api and user:
#         api.lists.unsubscribe(LIST_ID, {'email': user.email})
#         return True
#     else:
#         return False


class NewsletterUnsubscribeView(View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        action_type = request.POST.get('type')
        email = request.POST.get('data[email]')
        if action_type == 'unsubscribe' and email:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return HttpResponseNotFound(
                    "User with email {email} not found.".format(email=email)
                )
            user.unsubscribe()
            return HttpResponse(
                "User with email {email} has been unsubscribed.".format(email=email)
            )
        else:
            raise ValueError(
                'Cound not unsubscribe: action={action} email={email}'.format(action=action_type, email=email)
            )


class GroupRequiredMixin(AccessMixin):
    """
    CBV mixin which verifies that the current is in the required group.
    """
    required_group = 'Newsletter Moderators'

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        newsletter_group, created = Group.objects.get_or_create(name=self.required_group)
        if user and newsletter_group in user.groups.all():
            return super().dispatch(request, *args, **kwargs)
        else:
            return self.handle_no_permission()


class NewsletterManagementView(GroupRequiredMixin, TemplateView):
    template_name = 'newsletter/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get('filtered'):
            context['filtered'] = True
            filter = UserFilter(self.request.GET, queryset=User.objects.filter(newsletter=True))
            context['filter'] = filter
            context['emails'] = ', '.join(
                '{name} <{email}>'.format(name=user.name, email=user.email) for user in filter.qs)
            # context['emails'] = ', '.join(user.email for user in filter.qs)
            context['emails_counter'] = len(filter.qs)
        else:
            filter = UserFilter(self.request.GET, queryset=User.objects.none())
            context['filter'] = filter
        return context
