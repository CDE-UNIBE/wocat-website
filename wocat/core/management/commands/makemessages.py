# -*- coding: utf-8 -*-
import subprocess

from django.core.management.commands import makemessages


class Command(makemessages.Command):
    """
    Extended version of the default 'makemessages' command.

    - Pull the latest files from transifex
    - Create .po files (makemessages)
    - Push the files to transifex if desired.
    """

    def add_arguments(self, parser):
        super().add_arguments(parser)

    def handle(self, *args, **options):
        # Pull latest translations from transifex - unless specified otherwise.
        # if not options.get('do_create_only'):
        do_tx_pull = input('Force pull latest changes from transifex? [Y/n]')
        if do_tx_pull.lower() in ['', 'y']:
            print('Pulling latest changes from transifex ...')
            subprocess.call('tx pull --mode=developer -f', shell=True)

        print('Updating po files ...')
        super(Command, self).handle(*args, **options)

        do_tx_push = input(
            'Push the new translations to transifex? [Y/n]')
        if do_tx_push.lower() in ['', 'y']:
            print('Pushing latest changes to transifex ...')
            subprocess.call('tx push -s -t', shell=True)
