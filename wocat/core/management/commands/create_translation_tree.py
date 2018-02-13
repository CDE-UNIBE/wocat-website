# -*- coding: utf-8 -*-
from django.core.management import BaseCommand
from wagtail.wagtailcore.models import Page

from wocat.cms.models import ProjectPage


class Command(BaseCommand):
    help = 'Make a copy of the page tree in a new language and link ' \
           'translation pages.'
    original_locale = 'en'

    def error(self, msg):
        self.stdout.write(self.style.ERROR(msg))
        return

    def success(self, msg):
        self.stdout.write(self.style.SUCCESS(msg))

    def handle(self, *args, **options):

        try:
            orig_page = Page.objects.get(slug=self.original_locale)
            orig_id = orig_page.id
        except Page.DoesNotExist:
            orig_page = '-'
            orig_id = '?'

        orig_id_input = input(
            'ID of page to be copied (default: page with slug "{}") '
            '[{} | {}]: '.format(self.original_locale, orig_page, orig_id))
        if orig_id_input != '':
            try:
                orig_page = Page.objects.get(pk=orig_id_input)
            except (Page.DoesNotExist, ValueError):
                return self.error(
                    'No page with ID {} found.'.format(orig_id_input))

        to_page = orig_page.get_parent()

        to_id_input = input(
            'ID of page to copy to (default: parent of page to copy) '
            '[{} | {}]:'.format(to_page, to_page.id))
        if to_id_input != '':
            try:
                to_page = Page.objects.get(pk=to_id_input)
            except (Page.DoesNotExist, ValueError):
                return self.error(
                    'No page with ID {} found.'.format(to_id_input))

        new_locale = input('Locale code for new translation: ')
        if new_locale == '':
            self.stdout.write("No translation will be linked!")

        new_slug = input(
            'New slug of the copied page (default: the locale) [{}]: '.format(
                new_locale))
        if new_slug == '':
            if new_locale == '':
                return self.error('You must provide a slug.')
            new_slug = new_locale

        new_title = input(
            'New title of the copied page (usually the name of the language): ')
        if new_title == '':
            return self.error('You must provide a title.')

        recursive = input('Recursive (copy child pages as well)? [Y/n]: ')
        recursive = recursive.lower() != 'n'

        do_publish = input('Publish copied page(s)? [y/N]: ')
        do_publish = do_publish.lower() == 'y'

        update_attrs = {
            'slug': new_slug,
            'title': new_title,
        }
        self.copy_page(
            orig_page, to_page, locale=new_locale, recursive=recursive,
            update_attrs=update_attrs, do_publish=do_publish)

        self.success('OK')

    def copy_page(
            self, orig_page, to_page, locale='', recursive=False,
            update_attrs=None, do_publish=True):

        orig_specific_page = orig_page.specific

        # Recursive is always false. We want to create the translation links
        # first and do the recursive stuff manually.
        new_page = orig_specific_page.copy(
            recursive=False, to=to_page, update_attrs=update_attrs,
            copy_revisions=True, keep_live=do_publish)

        self.stdout.write('Copied page "{}" ({}) to "{}" ({})'.format(
            orig_specific_page, orig_specific_page.id, new_page, new_page.id))

        if locale != '':
            setattr(orig_specific_page, '{}_link'.format(locale), new_page)
            orig_specific_page.save()

        if type(orig_specific_page) == ProjectPage:
            # For project pages, also copy the included_countries
            new_page.included_countries.add(
                *list(orig_specific_page.included_countries.all()))
            new_page.save()

        if recursive is True:
            for child_page in orig_page.get_children():
                self.copy_page(
                    child_page, new_page, locale=locale, recursive=recursive,
                    update_attrs=None, do_publish=do_publish)
