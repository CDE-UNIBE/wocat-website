import logging

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.models import Group
from django.http import HttpResponse, Http404
from django.http import HttpResponseNotFound
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.views.generic import TemplateView

from .filters import UserFilter

User = get_user_model()
logger = logging.getLogger(__name__)


class NewsletterUnsubscribeView(View):
    """
    Unsubscribe webhook for MailChimp.
    """
    http_method_names = ['get', 'post']

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        """
        Very crude, but allow only MailChimp here. 
        """
        user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
        if user_agent == 'mailchimp.com':
            return super().dispatch(request, *args, **kwargs)
        else:
            logger.warning('Invalid user to access the Newsletter '
                        'unsubscribe hook: {}'.format(user_agent))
            raise Http404()

    def get(self, request, *args, **kwargs):
        """
        Empty response, so GET returns '200 success', which is required for the 
        'add webhook' form.
        """
        return HttpResponse()

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
        if user and (newsletter_group in user.groups.all() or user.is_superuser):
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
            context['emails'] = "\n".join(
                "{email}\t{name}".format(name=user.name, email=user.email) for user in filter.qs)
            # context['emails'] = ', '.join(user.email for user in filter.qs)
            context['emails_counter'] = len(filter.qs)
        else:
            filter = UserFilter(self.request.GET, queryset=User.objects.none())
            context['filter'] = filter
        return context
