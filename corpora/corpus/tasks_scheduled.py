from celery.schedules import crontab

# Will need to add "celery -A proj beat" for these to run.
# this needs to run on the webserver
# celery -A proj beat -s /webapp/logs/celery/celerybeat-schedule

CELERYBEAT_SCHEDULE = {
    'set_recording_duration': {
        'task': 'corpus.tasks.set_all_recording_durations',
        'schedule': crontab(minute='*'),
    },
}