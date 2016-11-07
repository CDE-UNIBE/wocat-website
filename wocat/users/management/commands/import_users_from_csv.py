import csv

from django.core.management.base import BaseCommand
from django.db import DataError

from wocat.institutions.models import Institution
from wocat.users.models import User


class Command(BaseCommand):
    help = 'Create a tree-like structure showing which template includes which'

    def handle(self, *args, **options):
        # self.import_institutions()
        self.import_users()

    def import_institutions(self):
        Institution.objects.all().delete()
        f = open('export_users_institutions_20160819/wocat_institution_export.csv')
        fieldnames = ['id', 'name', 'url', 'country', 'contact_user']
        read = csv.DictReader(f, delimiter=';', fieldnames=fieldnames)
        next(read)
        for row in read:
            # print(row)
            if not row['name'].strip():
                print(row)
            if not Institution.objects.filter(id=row['id']):
                i1 = Institution.objects.create(
                    id=row['id'],
                    name=row['name'],
                    abbreviation=row['name'],
                    url=row['url'],
                    # country=row['country'], TODO
                )

    def import_users(self):
        f = open('export_users_institutions_20160819/wocat_user_export_all.csv')
        fieldnames = [
            'uid', 'username', 'title', 'firstname', 'lastname', 'gender', 'lang', 'second_email',
            'phone', 'mobile', 'fax', 'country', 'city', 'zip', 'address', 'second_address', 'position',
            'department', 'institution_id', 'quest_id', 'creation_date', 'lastlogin', 'password'
        ]
        read = csv.DictReader(f, delimiter=';', fieldnames=fieldnames)
        next(read)
        for row in read:
            # print(row)
            if not User.objects.filter(email=row['username']) \
                and not User.objects.filter(id=row['uid']):
                try:
                    u1 = User.objects.create(
                        id=row['uid'],
                        email=row['username'],
                        title=row['title'],
                        first_name=row['firstname'],
                        last_name=row['lastname'],
                        second_email=row['second_email'],
                        phone=row['phone'],
                        phone_2=row['mobile'],
                        fax=row['fax'],
                        city=row['city'],
                        postal_code=row['zip'],
                        address=row['address'],
                        address_2=row['second_address'],
                        position=row['position'],
                        department=row['department'],
                    )
                    u1.gender = row['gender'] if row['gender'] in ['m', 'f'] else None
                    u1.language = 'de' if row['lang'] == 'DE' else 'en'

                    if not row['institution_id'] in ['0', 'NULL']:
                        u1.institution = Institution.objects.get(id=row['institution_id'])
                    # TODO: row['quest_id']?
                    # u1.country = TODO !
                    u1.save()
                except DataError:
                    print(row)
                except:
                    print(row)
                    import ipdb;
                    ipdb.set_trace()


                    # u1 = User.objects.first()
                    # print(u1)
                    # import ipdb; ipdb.set_trace()
                    # print(u1)
