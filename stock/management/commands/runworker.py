from django.core.management.base import BaseCommand
import subprocess


class Command(BaseCommand):
    help = "Runs the Celery worker"

    def handle(self, *args, **options):
        self.stdout.write("Starting Celery worker...")
        subprocess.call(["celery", "-A", "stock", "worker", "-l", "info"])
