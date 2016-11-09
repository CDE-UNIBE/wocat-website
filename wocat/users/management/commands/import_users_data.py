import csv

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand
from django.core.validators import EmailValidator
from django.db import DataError
from django.db import IntegrityError
from django.utils import timezone

from wocat.countries.models import Country
from wocat.institutions.models import Institution
from wocat.users.forms import FullUserForm as UserForm
from wocat.users.models import User


class Command(BaseCommand):
    help = 'Import user data from a csv file.'

    def handle(self, *args, **options):
        self.import_institutions(init=True)
        self.import_users()
        self.import_institutions()

    def import_institutions(self, init=False):
        print('>> Importing insttitutions...')
        file = open('local/export_users_institutions_20160819/wocat_institution_export.csv')
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
                print('WARNING: No name: ', row)
                warnings += 1
            try:
                country = Country.objects.get(code=row['country'])
            except Country.DoesNotExist:
                print('WARNING: Country code `{0}` not found: `{1}`'.format(row['country'], row))
                warnings += 1
                country = None
            try:
                contact_person = get_user_model().objects.get(id=row['contact_user'])
            except get_user_model().DoesNotExist:
                if not init:
                    print('WARNING: User id `{0}` not found: `{1}`'.format(row['contact_user'], row))
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
        print('Warnings: {0}'.format(warnings))
        print('Created: {0}'.format(created))
        print('Updated: {0}'.format(updated))

    def import_users(self):
        print('>> Importing users...')
        file = open('local/export_users_institutions_20160819/wocat_user_export_all.csv')
        fieldnames = [
            'uid', 'username', 'title', 'firstname', 'lastname', 'gender', 'lang', 'second_email',
            'phone', 'mobile', 'fax', 'country', 'city', 'zip', 'address', 'second_address', 'position',
            'department', 'institution_id', 'quest_id', 'creation_date', 'lastlogin', 'password'
        ]
        read = csv.DictReader(file, delimiter=';', fieldnames=fieldnames)
        next(read)
        # User.objects.exclude(id=1).delete()
        for row in read:

            id = row['uid']
            email = row['username']

            if not User.objects.filter(email=email) and not User.objects.filter(id=id):
                # print(row)
                data = {}
                data['id'] = id
                data['email'] = email
                data['title'] = row['title']
                data['first_name'] = row['firstname']
                data['last_name'] = row['lastname']
                data['second_email'] = row['second_email']
                data['phone'] = row['phone']
                data['phone_2'] = row['mobile']
                data['fax'] = row['fax']
                data['city'] = row['city']
                data['postal_code'] = row['zip']
                data['address'] = row['address']
                data['address_2'] = row['second_address']
                data['position'] = row['position']
                data['department'] = row['department']
                data['password'] = row['password']

                # Handle language
                try:
                    data['language'] = self.clean_language(row['lang'])
                except ValidationError as error:
                    default_language = 'en'
                    self.warn(id,
                              '{message} - Using "{default}".'.format(message=error.message, default=default_language))
                    data['language'] = default_language
                # Accept terms and conditions
                data['terms_and_conditions'] = True
                # Handle gender
                try:
                    data['gender'] = self.clean_gender(row['gender'])
                except ValidationError as error:
                    default_gender = User.MALE
                    self.warn(id,
                              '{message} - Using "{default}".'.format(message=error.message, default=default_gender))
                    data['gender'] = default_gender
                # Handle Institution
                try:
                    data['institution'] = self.clean_institution(row['institution_id'])
                except ValidationError as error:
                    default_institution = None
                    self.warn(id,
                              '{message} - Using "{default}".'.format(message=error.message,
                                                                      default=default_institution))
                    data['institution'] = default_institution
                # Handle Country
                try:
                    data['country'] = self.clean_country(row['country'])
                except ValidationError as error:
                    default_country = None
                    self.warn(id,
                              '{message} - Using "{default}".'.format(message=error.message, default=default_country))
                    data['country'] = default_country
                # Handle Creation Date
                try:
                    data['date_joined'] = self.clean_date_joined(row['creation_date'])
                except ValidationError as error:
                    default_date_joined = timezone.now()
                    self.warn(id,
                              '{message} - Using "{default}".'.format(message=error.message,
                                                                      default=default_date_joined))
                    data['date_joined'] = default_date_joined
                # Handle Email
                try:
                    data['email'] = self.clean_email(email)
                except ValidationError as error:
                    self.error(id,
                               '{message} - Skipping.'.format(message=error.message))
                    continue

                form = UserForm(data)
                if form.is_valid():
                    try:
                        cleaned_data = form.cleaned_data
                        # forcing the custom id
                        cleaned_data['id'] = id
                        User.objects.create(**cleaned_data)
                    except IntegrityError as error:
                        self.error(id, 'Import failed: {0}'.format(error))
                else:
                    self.error(id, 'Import failed: {0}'.format(dict(form.errors)))
            else:
                self.error(id, 'Email or id exists already.')

    @staticmethod
    def clean_language(value):
        language_map = {
            'EN': 'en',
            'FR': 'fr',
            'ES': 'es',
        }
        language = language_map.get(value)
        if language:
            return language
        raise ValidationError('Language "{0}" not found.'.format(value))

    @staticmethod
    def clean_gender(value):
        if value in [User.MALE, User.FEMALE]:
            return value
        raise ValidationError('Gender "{0}" not found.'.format(value))

    @staticmethod
    def clean_institution(value):
        try:
            value = int(value)
        except ValueError:
            pass
        if value and value in Institution.objects.values_list('id', flat=True):
            return value
        raise ValidationError('Institution with id "{0}" not found.'.format(value))

    @staticmethod
    def clean_country(value):
        try:
            return Country.objects.get(pk=value).pk
        except Country.DoesNotExist:
            raise ValidationError('Country "{0}" not found.'.format(value))

    @staticmethod
    def clean_date_joined(value):
        try:
            return timezone.datetime.fromtimestamp(int(value))
        except:
            raise ValidationError('Join date "{0}" not found.'.format(value))

    @staticmethod
    def clean_email(value):
        try:
            EmailValidator()(value)
            return value
        except:
            raise ValidationError('Email "{0}" invalid.'.format(value))

    @staticmethod
    def warn(id, message):
        print('WARNING: ID:{0} - {1}'.format(id, message))

    @staticmethod
    def error(id, message):
        print('ERROR: ID:{0} - {1}'.format(id, message))
