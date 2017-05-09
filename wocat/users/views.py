# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import contextlib

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _

from mama_cas.views import LoginView

from wocat.users.forms import UserForm
from .models import User


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by email
    #slug_field = 'email'
    #slug_url_kwarg = 'email'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user

        from wocat.cms.models import MembersPage
        members_page = MembersPage.objects.first()
        if members_page:
            members_url = members_page.url
        else:
            members_url = ''
        users_teaser_data = {
            'href': '{0}#{1}'.format(members_url, user.country.code if user.country else ''),
            'external': False,
            'title': _('WOCAT members from your country'),
            'description': _('Find other WOCAT members from your country or search for WOCAT members worldwide.'),
            'readmorelink': {'text': _(' Discover members of the WOCAT Network')},
            'imgsrc': '',
            'imgpos': '',
            'largeimg': '',
            'lines': True,
        }
        users_teaser = render_to_string('widgets/teaser.html', context=users_teaser_data)
        context['users_teaser'] = users_teaser

        qcat_teaser_data = {
            'href': 'https://qcat.wocat.net/en/accounts/user/{0}/'.format(user.id),
            'external': False,
            'title': _('My SLM Data'),
            'description': _('Go to the Global SLM Database and see your own SLM Practices.'),
            'readmorelink': {'text': _('Go to the SLM Database')},
            'imgsrc': '',
            'imgpos': '',
            'largeimg': '',
            'lines': True,
        }
        qcat_teaser = render_to_string('widgets/teaser.html', context=qcat_teaser_data)
        context['qcat_teaser'] = qcat_teaser
        return context


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail', kwargs={'pk': self.request.user.id})


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm

    def get_success_url(self):
        return reverse('users:detail', kwargs={'pk': self.request.user.id})

    def get_object(self):
        return User.objects.get(email=self.request.user.email)


class UserListView(LoginRequiredMixin, ListView):
    model = User


class CASLoginView(LoginView):

    def form_invalid(self, form):
        """
        For inactive users: redirect to 're-activate' view.
        """
        with contextlib.suppress(User.DoesNotExist):
            user = User.objects.get(email=form.cleaned_data['username'])
            if not user.is_active:
                return HttpResponseRedirect(reverse('account_inactive'))
        return super().form_invalid(form=form)
