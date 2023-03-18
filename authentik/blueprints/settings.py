"""blueprint Settings"""
from celery.schedules import crontab

from authentik.lib.utils.time import fqdn_rand

from authentik.lib.utils.cron import get_task_period

blueprints_discovery_period = get_task_period(
    "blueprints_discovery", {"minute": fqdn_rand("blueprints_v1_discover"), "hour": "*"}
)

clear_failed_blueprints_period = get_task_period(
    "clear_failed_blueprints", {"minute": fqdn_rand("blueprints_v1_cleanup"), "hour": "*"}
)

CELERY_BEAT_SCHEDULE = {
    "blueprints_v1_discover": {
        "task": "authentik.blueprints.v1.tasks.blueprints_discovery",
        "schedule": crontab(**blueprints_discovery_period),
        "options": {"queue": "authentik_scheduled"},
    },
    "blueprints_v1_cleanup": {
        "task": "authentik.blueprints.v1.tasks.clear_failed_blueprints",
        "schedule": crontab(**clear_failed_blueprints_period),
        "options": {"queue": "authentik_scheduled"},
    },
}
