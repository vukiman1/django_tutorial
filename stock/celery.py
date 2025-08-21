# Cập nhật cấu hình Celery
from celery import Celery
from celery.schedules import crontab
import os
from stock.service.cron_service import save_bitcoin_data

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo_app.settings")

app = Celery("stock")
app.config_from_object("todo_app.settings.CELERY")

app.autodiscover_tasks()


@app.task
def test(arg):
    print(arg)


@app.task
def add(x, y):
    z = x + y
    print(z)


@app.task
def bitcoin_task():
    save_bitcoin_data()
