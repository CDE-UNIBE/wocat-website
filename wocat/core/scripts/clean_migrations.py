from django.conf import settings
from django.core.management import call_command
from django.db.migrations.recorder import MigrationRecorder


def run():
    # squashing migrations in the cms app caused problems with the
    # migrationhistory. this is a brute way of creating new migrations.
    # app_labels = [label.strip('wocat.') for label in settings.LOCAL_APPS]
    app_labels = ['cms', 'news']
    MigrationRecorder.Migration.objects.filter(
        app__in=app_labels
    ).delete()
    for app in app_labels:
        call_command('migrate', app, '--fake')
