default_app_config = 'rickshaw.apps.RickshawConfig'

from django.conf import settings

print("\nChecking Rickshaw Configuration...")

if settings.RICKSHAW_CELERY is not True:
    print('Rickshaw - Cron Tasks will need to be setup, see documentation \n')
else:
    print('Rickshaw - Celery Async Tasks will be used \n')
