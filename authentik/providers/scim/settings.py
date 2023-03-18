"""SCIM task Settings"""
from celery.schedules import crontab

from authentik.lib.utils.time import fqdn_rand

from authentik.lib.utils.cron import get_task_period

scim_sync_all_period = get_task_period(
    "scim_sync_all", {'minute': fqdn_rand("scim_sync_all"), 'hour':"*"}
)

CELERY_BEAT_SCHEDULE = {
    "providers_scim_sync": {
        "task": "authentik.providers.scim.tasks.scim_sync_all",
        "schedule": crontab(**scim_sync_all_period),
        "options": {"queue": "authentik_scheduled"},
    },
}
