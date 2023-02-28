from __future__ import absolute_import ,unicode_literals
from celery import Celery
import os
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AuthomatizationBusines.settings')
app = Celery('AuthomatizationBusines')
app.config_from_object('django.conf:settings',namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-spam-every-1-minute': {
        'task': 'customuser.tasks.send_beat_email',
        'schedule': crontab(minute='*/1'),
    },
}
 