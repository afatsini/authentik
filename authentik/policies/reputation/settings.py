"""Reputation Settings"""
from celery.schedules import crontab

from authentik.lib.utils.cron import get_task_period

save_reputation_period = get_task_period(
    "save_reputation", {'minute': "1-59/5"}
)

CELERY_BEAT_SCHEDULE = {
    "policies_reputation_save": {
        "task": "authentik.policies.reputation.tasks.save_reputation",
        "schedule": crontab(**save_reputation_period),
        "options": {"queue": "authentik_scheduled"},
    },
}
