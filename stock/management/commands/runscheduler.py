from celery.schedules import crontab
from stock.celery import app, test, bitcoin_task
from celery import Celery
from django.core.management.base import BaseCommand
import subprocess


@app.on_after_configure.connect
def setup_periodic_tasks(sender: Celery, **kwargs):

    # Task chạy mỗi phút - sử dụng số giây
    # sender.add_periodic_task(
    #     60.0,
    #     test.s("Chạy task mỗi 1 phút"),
    #     name="add every 1 phút",
    # )

    # # Task chạy mỗi 10 giây
    # sender.add_periodic_task(
    #     10.0,
    #     test.s("Chạy task mỗi 10s"),
    #     name="add every 10s",
    # )

    sender.add_periodic_task(
        30.0,
        bitcoin_task.s(),
        name="bitcoin task",
    )


class Command(BaseCommand):
    help = "Runs the Celery beat scheduler"

    def handle(self, *args, **options):
        self.stdout.write("Starting Celery beat...")
        subprocess.call(["celery", "-A", "stock", "beat", "-l", "info"])
