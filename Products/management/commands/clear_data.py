from django.core.management.base import BaseCommand
from django.db import connection
from django.apps import apps

class Command(BaseCommand):
    help = 'Forcefully delete all data from the database'

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            # Get all models from all installed apps
            all_models = apps.get_models()
            for model in all_models:
                table_name = model._meta.db_table
                cursor.execute(f'TRUNCATE TABLE "{table_name}" CASCADE;')

        self.stdout.write(self.style.SUCCESS('Successfully deleted all data from the database.'))
