import contextlib
import csv
import collections
import re

from django.apps import apps
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand
from django.core.validators import EmailValidator
from django.db import IntegrityError, connections
from django.utils import timezone

from wocat.countries.models import Country
from wocat.institutions.models import Institution
from wocat.users.forms import FullUserForm as UserForm
from wocat.users.models import User


ErrorString = collections.namedtuple('ErrorString', 'email id step text')


class FieldInfo:

    def __init__(self, old_name, new_name='', extra=None):
        self.old_name = old_name
        self.new_name = new_name or old_name
        self.extra = extra

    def __str__(self):
        return self.old_name

    def get_value(self, row):
        value = row[self.old_name]
        if self.extra:
            value = getattr(Command, self.extra)(value)
        return value


class Command(BaseCommand):
    help = 'Import user data from a csv file.'

    field_definitions = [
        FieldInfo('uid', 'id', 'clean_id'),
        FieldInfo('username', 'email', 'clean_email'),
        FieldInfo('hidden', 'is_active', 'clean_bool'),
        FieldInfo('user_disable', 'is_active', 'clean_bool'),
        FieldInfo('user_deleted', 'is_active', 'clean_bool'),
        FieldInfo('address_deleted', 'ignore_this'),
        FieldInfo('title'),
        FieldInfo('firstname', 'first_name'),
        FieldInfo('lastname', 'last_name'),
        FieldInfo('gender', 'gender', 'clean_gender'),
        FieldInfo('lang', 'language', 'clean_language'),
        FieldInfo('second_email', 'second_email', 'clean_email'),
        FieldInfo('phone', 'phone'),
        FieldInfo('mobile', 'phone_2'),
        FieldInfo('fax', 'fax'),
        FieldInfo('country', 'country', 'clean_country'),
        FieldInfo('city', 'city'),
        FieldInfo('zip', 'zip'),
        FieldInfo('address', 'address'),
        FieldInfo('second_address'),
        FieldInfo('position'),
        FieldInfo('department'),
        FieldInfo('institution_id'),
        FieldInfo('quest_id'),
        FieldInfo('creation_date', 'date_joined', 'clean_date_joined'),
        FieldInfo('lastlogin'),
        FieldInfo('status')
    ]
    errors = []
    success = []
    warnings = []

    @property
    def fieldnames(self):
        return [field.__str__() for field in self.field_definitions]

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('institutions', nargs='+', type=str)
        parser.add_argument('users', nargs='+', type=str)

    def handle(self, *args, **options):
        verbosity = int(options.get('verbosity', 0))
        self.stdout.write('!! Import of institutions has been temporarily disabled !!')
        # self.import_institutions(filename=options['institutions'][0], init=True)
        self.import_users(filename=options['users'][0])
        # self.import_institutions(filename=options['institutions'][0])
        self.reset_sql_sequences(verbosity)
        self.print_results(verbosity)

    def import_institutions(self, filename, init=False):
        self.stdout.write('Importing institutions...')
        file = open(filename)
        fieldnames = ['id', 'name', 'url', 'country', 'contact_user']
        read = csv.DictReader(file, delimiter=';', fieldnames=fieldnames)
        next(read)
        warnings = 0
        created = 0
        updated = 0
        for row in read:
            # print(row)
            id = row['id']
            name = row['name'].strip()
            abbreviation = name
            url = row['url']
            if not name:
                self.stdout.write('WARNING: No name: {}'.format(row['id']))
                warnings += 1
            try:
                country = Country.objects.get(code=row['country'])
            except Country.DoesNotExist:
                self.stdout.write('WARNING: Country code `{0}` not found: `{1}`'.format(row['country'], row))
                warnings += 1
                country = None
            try:
                contact_person = get_user_model().objects.get(id=row['contact_user'])
            except get_user_model().DoesNotExist:
                if not init:
                    self.stdout.write('WARNING: User id `{0}` not found: `{1}`'.format(row['contact_user'], row))
                    warnings += 1
                contact_person = None
            # print(id, name, abbreviation, url, country, contact_person)
            if not Institution.objects.filter(id=id).exists():
                Institution.objects.create(
                    id=id,
                    name=name,
                    abbreviation=abbreviation,
                    url=url,
                    country=country,
                    contact_person=contact_person
                )
                created += 1
            else:
                institution = Institution.objects.get(id=id)
                if not institution.contact_person:
                    institution.contact_person = contact_person
                institution.save()
                updated += 1
        self.stdout.write('Warnings: {0}'.format(warnings))
        self.stdout.write('Created: {0}'.format(created))
        self.stdout.write('Updated: {0}'.format(updated))

    def import_users(self, filename):
        self.stdout.write('Importing users...')
        id_to_email = {}
        with open(filename) as file:

            read = csv.DictReader(file, fieldnames=self.fieldnames, delimiter=';')
            next(read)

            for row in read:
                data = dict(self.get_imported_row(row))
                # multiple fields affect 'is_active'
                data['is_active'] = False
                data['newsletter'] = True
                user_form = UserForm(data=data)
                if user_form.is_valid():
                    self.update_or_create_user(
                        email=data['email'], **user_form.cleaned_data
                    )
                    id_to_email[data['id']] = data['email']
                    self.success.append(data['email'])
                else:
                    self.errors.append(
                        ErrorString(
                            email=data.get('email', ''),
                            id=data.get('id', ''),
                            step='validation',
                            text=user_form.errors)
                    )

        self.update_user_ids(id_to_email)

    def reset_sql_sequences(self, verbosity):
        connection = connections['default']
        models = apps.get_app_config('users').get_models(include_auto_created=True)
        statements = connection.ops.sequence_reset_sql(self.style, models)
        if verbosity > 1:
            self.stdout.write('Updating sql sequences:\n')
            self.stdout.write('\n'.join(statements))
        with connection.cursor() as c:
            for statement in statements:
                no_newlines = re.sub('\x1b.*?m', '', statement)
                c.execute(no_newlines)

    def _get_is_active(self, **row):
        for key in ['user_disable', 'user_deleted', 'hidden']:
            if row[key] in ['1', 1]:
                return False
        return True

    def get_imported_row(self, row: dict):
        for field in self.field_definitions:
            try:
                yield field.new_name, field.get_value(row)
            except ValidationError as e:
                self.errors.append(ErrorString(
                    email=row['username'],
                    id=row.get('id', ''),
                    step='reading csv',
                    text=e)
                )

    def print_results(self, verbosity: int):
        self.stdout.write('Report:\n')
        self.stdout.write('Successfull imports: {}\n'.format(len(self.success)))
        self.stdout.write('Warnings raised: {}\n'.format(len(self.warnings)))
        self.stdout.write('Errors: {}\n'.format(len(self.errors)))

        if verbosity > 1:
            self.stdout.write('--------------------\n')
            self.stdout.write('Successful imports: \n')
            self.stdout.write('--------------------\n')
            for success in self.success:
                self.stdout.write(success)

            self.stdout.write('--------------------\n')
            self.stdout.write('Warnings:           \n')
            self.stdout.write('--------------------\n')
            for warning in self.warnings:
                self.stdout.write(warning)

        self.stdout.write('--------------------\n')
        self.stdout.write('Errors:             \n')
        self.stdout.write('--------------------\n')
        for error in self.errors:
            self.stdout.write('id: {} \t| email {} \t| step {}'.format(
                error.id, error.email, error.step
            ))
            if verbosity > 1:
                self.stdout.write(str(error.text))
            self.stdout.write('\n')

    @staticmethod
    def update_or_create_user(email, **data):
        del data['key_work_topics']
        del data['experiences']
        del data['user_permissions']
        del data['groups']
        User.objects.update_or_create(email=email, defaults=data)

    def update_user_ids(self, id_to_email):
        """
        user.id is read-only, this is a workaround to update the id.
        """
        for user_id, email in id_to_email.items():
            # shift id if already existing for another user.
            with contextlib.suppress(User.DoesNotExist):
                blocked = User.objects.get(id=user_id)
                max_id = User.objects.order_by('id').last().id
                self._update_user_id(user_id=max_id + 1, email=blocked.email)
            self._update_user_id(user_id=user_id, email=email)

        # Re-check all ids.
        for user_id, email in id_to_email.items():
            try:
                User.objects.get(email=email, id=user_id)
            except User.DoesNotExist:
                raise User.DoesNotExist(
                    'something went wrong when fixing the ids: %s %s' %
                    email, user_id
                )

    def _update_user_id(self, user_id, email):
        try:
            User.objects.filter(email=email).update(id=user_id)
        except IntegrityError as e:
            self.errors.append(ErrorString(
                email=email,
                id=user_id,
                step='database query',
                text=e)
            )

    @classmethod
    def clean_id(cls, value):
        # this must be loud, and fixed manually.
        return int(value)

    @classmethod
    def clean_language(cls, value):
        language_map = {
            'EN': 'en',
            'FR': 'fr',
            'ES': 'es',
        }
        try:
            return language_map[value]
        except KeyError:
            cls.warnings.append('Language "{0}" not found.'.format(value))
        finally:
            return 'en'

    @classmethod
    def clean_gender(cls, value):
        gender_mapping = {
            "0": User.MALE,
            "1": User.FEMALE,
        }
        value = gender_mapping.get(value, value)
        if value in [User.MALE, User.FEMALE]:
            return value
        cls.warnings.append('Gender "{0}" not found.'.format(value))
        return ''

    @classmethod
    def clean_institution(cls, value):
        try:
            value = int(value)
        except (TypeError, ValueError):
            pass
        if value and value in Institution.objects.values_list('id', flat=True):
            return value
        cls.warnings.append(('Institution with id "{0}" not found.'.format(value)))
        return None

    @classmethod
    def clean_country(cls, value):
        try:
            return Country.objects.get(code=value).pk
        except Country.DoesNotExist:
            cls.warnings.append(('Country "{0}" not found.'.format(value)))
            return ''

    @classmethod
    def clean_date_joined(cls, value):
        try:
            return timezone.datetime.fromtimestamp(int(value))
        except:
            cls.warnings.append('Join date "{0}" not found.'.format(value))
        finally:
            return timezone.datetime.now()

    @classmethod
    def clean_email(cls, value):
        if not value or value == 'NULL':
            return ''
        try:
            EmailValidator()(value)
            return value
        except ValidationError:
            # ValidationErrors are expected in the calling method, so raise a
            # different error...
            raise ValueError('invalid email: %s' % value)

    @classmethod
    def clean_bool(cls, value):
        return value in ['1', 'true', 'True', 1]
