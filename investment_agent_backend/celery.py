import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "investment_agent_backend.settings")

app = Celery("investment_agent_backend")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()