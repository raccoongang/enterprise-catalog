"""
Defines the Celery application for the enterprise_catalog project
"""
from celery import Celery
from django.conf import settings


app = Celery('enterprise_catalog', )
app.conf.task_protocol = 1

# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object(settings)

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


if __name__ == '__main__':
    app.start()
