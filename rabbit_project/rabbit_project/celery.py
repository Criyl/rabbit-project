import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rabbit_project.settings')

app = Celery('rabbit_project',
             broker='rpc://admin:pass@rabbitmq:5672',
             backend='rpc://')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
