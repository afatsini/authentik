"""authentik admin settings"""
from celery.schedules import crontab

from authentik.lib.utils.time import fqdn_rand

from authentik.lib.utils.cron import get_task_period

update_latest_version_period = get_task_period(
    "update_latest_version", {"minute": fqdn_rand("admin_latest_version"), "hour": "*"}
)

CELERY_BEAT_SCHEDULE = {
    "admin_latest_version": {
        "task": "authentik.admin.tasks.update_latest_version",
        "schedule": crontab(**update_latest_version_period),
        "options": {"queue": "authentik_scheduled"},
    }
}
