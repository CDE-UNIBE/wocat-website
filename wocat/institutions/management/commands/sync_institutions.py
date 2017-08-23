# -*- coding: utf-8 -*-
import csv

import os
from django.core.management import BaseCommand, call_command
from django.db import connection

from wocat.countries.models import Country
from wocat.institutions.models import Institution


class Command(BaseCommand):
    """
    This command should only run once to copy institutions which were entered
    only in QCAT to the new WOCAT CMS. From there on, the CMS is authoritative:
    New institutions can only be added there and institutions are synced
    periodically to QCAT.

    -- SQL Query to extract the necessary data from QCAT:
    SELECT
        configuration_institution.id, name, abbreviation, country_id, keyword
    FROM configuration_institution
    INNER JOIN configuration_value
        ON configuration_institution.country_id = configuration_value.id
    WHERE configuration_institution.id >= 956;

    Save the results as CSV, then run script as:
        python manage.py sync_institutions /path/to/file.csv
    """
    errors = []

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('institutions_file', nargs='+', type=str)

    def handle(self, *args, **options):

        institutions = self.read_institutions(options['institutions_file'][0])

        for institution in institutions:
            self.create_institution(institution)

        self.reset_sql_sequences()

        for error in self.errors:
            self.stdout.write('Error: {}'.format(error))

    @staticmethod
    def read_institutions(filename):
        file = open(filename)
        fieldnames = ['id', 'name', 'abbreviation', 'country_id', 'country_code']
        read = csv.DictReader(file, delimiter=';', fieldnames=fieldnames)

        for row in read:
            # Only institutions with ID >= 956 should be imported from QCAT to
            # the CMS. SQL query should already filter it out, but it doesn't
            # hurt to double check ...
            if int(row['id']) >= 956:
                yield row

    def create_institution(self, institution):

        country_code = institution['country_code'].replace('country_', '')
        country = Country.objects.get(code=country_code)

        institution_object, created = Institution.objects.get_or_create(
            pk=institution['id'], defaults={
                'name': institution['name'],
                'abbreviation': institution['abbreviation'],
                'country': country,
            })
        if created is False:
            self.errors.append(
                'Institution {} already exists in the CMS!'.format(
                    institution['id']))

    @staticmethod
    def reset_sql_sequences():
        os.environ['DJANGO_COLORS'] = 'nocolor'
        cursor = connection.cursor()
        cursor.execute(call_command('sqlsequencereset', 'institutions'))
