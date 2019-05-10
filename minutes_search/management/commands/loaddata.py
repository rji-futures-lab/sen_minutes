import os
from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import DataError
from minutes_search.models import witness_for, witness_against
from django.core.management import call_command

class Command(BaseCommand):
    """
    Loads Senate minutes into PostgreSQL database
    """

    def handle(self, *args, **kwargs):
        self.stdout.write('Flushing data...', ending='')
        management.call_command(
            'flush', verbosity=0, interactive=False,
        )
        self.stdout.write(
            self.style.SUCCESS('OK')
        )
        insert_count = witness_for.objects.from_csv(os.path.join(
            settings.DATA_DIR, 'witness_for.csv')
        )
        print("{} records inserted".format(insert_count))

        insert_count_2 = witness_against.objects.from_csv(os.path.join(
            settings.DATA_DIR, 'witness_against.csv')
        )
        print("{} records inserted".format(insert_count_2))
