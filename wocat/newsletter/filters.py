import django_filters
from django import forms
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from wocat.countries.models import Country
from wocat.institutions.models import Institution

User = get_user_model()

positions = User.objects.order_by('position').values_list('position', flat=True).distinct()
departments = User.objects.order_by('department').values_list('department', flat=True).distinct()
cities = User.objects.order_by('city').values_list('city', flat=True).distinct()

ALL_CHOICE = (('', 'all'),)

BLANK_CHOICE = (('', '---'),)

NONE_CHOICE = ((None, '---'),)


class UserFilter(django_filters.FilterSet):
    is_staff = django_filters.BooleanFilter()
    is_active = django_filters.BooleanFilter()
    gender = django_filters.ChoiceFilter(
        label=_('Salutation'),
        choices=ALL_CHOICE + User.GENDER_CHOICES
    )
    position = django_filters.MultipleChoiceFilter(
        choices=(tuple((position, position) for position in positions if position))
    )
    department = django_filters.MultipleChoiceFilter(
        choices=(tuple((department, department) for department in departments if department))
    )
    function = django_filters.MultipleChoiceFilter(
        choices=User.FUNCTION_CHOICES
    )
    city = django_filters.MultipleChoiceFilter(
        choices=(tuple((city, city) for city in cities if city))
    )
    country = django_filters.ModelMultipleChoiceFilter(
        queryset=Country.objects.all()
        # choices=(tuple((city, city) for city in cities if city))
    )
    institution = django_filters.ModelMultipleChoiceFilter(
        queryset=Institution.objects.all()
        # choices=(tuple((city, city) for city in cities if city))
    )

    class Meta:
        model = User
        fields = [
            'gender', 'position', 'department', 'function', 'experiences', 'key_work_topics',
            'postal_code', 'city', 'country', 'language', 'institution',
            'is_staff', 'is_active'
        ]
        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
        }
