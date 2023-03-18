"""Event Settings"""
from celery.schedules import crontab

from authentik.lib.utils.time import fqdn_rand

from authentik.lib.utils.cron import get_task_period

notification_cleanup_period = get_task_period(
    "notification_cleanup", {'minute': fqdn_rand("notification_cleanup"), 'hour':"*/8"}
)

CELERY_BEAT_SCHEDULE = {
    "events_notification_cleanup": {
        "task": "authentik.events.tasks.notification_cleanup",
        "schedule": crontab(**notification_cleanup_period),
        "options": {"queue": "authentik_scheduled"},
    },
}
