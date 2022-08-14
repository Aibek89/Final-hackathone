import os

import django
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_net.settings')
django.setup()
app = Celery('social_net')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


app.conf.beat_schedule = {
    'send_spam_from_makers': {
        'task': 'post.tasks.spam_email',
        'schedule': crontab(minute='*/1')
    }
}