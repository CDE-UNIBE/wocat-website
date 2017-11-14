from django.core.management.commands.runserver import Command as RunServer


class Command(RunServer):
    """
    Restarting the runserver is painfully slow during development due to huge
    migration files (--> wagtail). This is a development helper.
    """
    def check_migrations(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("SKIPPING MIGRATION CHECKS!\n"))
