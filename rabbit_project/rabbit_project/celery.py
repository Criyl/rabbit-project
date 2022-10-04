import os
from celery import Celery
from kombu import Exchange, Queue, binding

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rabbit_project.settings')

app = Celery('rabbit_project',
             broker='rpc://admin:pass@rabbitmq:5672',
             backend='rpc://')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

default_exchange = Exchange('default', type='direct')
special_exchange = Exchange('special', type='direct')

app.conf.task_queues = (
    Queue('default', default_exchange, routing_key='default'),
    Queue('special', special_exchange, routing_key='special'),
)
app.conf.task_default_queue = 'default'
app.conf.task_default_exchange = 'default'
app.conf.task_default_routing_key = 'default'
