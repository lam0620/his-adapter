
from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Load data code permission'

    def handle(self, *args, **kwargs):
        main_url = "apps/shared/data/"
        list_data = [
            "code_permission.json",
            "integration_app.json",
        ]
        for data in list_data:
            call_command("loaddata", main_url + data)
