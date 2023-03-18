"""Outposts Settings"""
from celery.schedules import crontab

from authentik.lib.utils.time import fqdn_rand

from authentik.lib.utils.cron import get_task_period

outpost_controller_all_period = get_task_period(
    "outpost_controller_all", {"minute": fqdn_rand("outposts_controller"), "hour": "*/4"}
)

outpost_service_connection_monitor_period = get_task_period(
    "outpost_service_connection_monitor", {"minute": "3-59/15"}
)

outpost_token_ensurer_period = get_task_period(
    "outpost_token_ensurer", {"minute": fqdn_rand("outpost_token_ensurer"), "hour": "*/8"}
)

outpost_connection_discovery_period = get_task_period(
    "outpost_connection_discovery",
    {"minute": fqdn_rand("outpost_connection_discovery"), "hour": "*/8"},
)

CELERY_BEAT_SCHEDULE = {
    "outposts_controller": {
        "task": "authentik.outposts.tasks.outpost_controller_all",
        "schedule": crontab(**outpost_controller_all_period),
        "options": {"queue": "authentik_scheduled"},
    },
    "outposts_service_connection_check": {
        "task": "authentik.outposts.tasks.outpost_service_connection_monitor",
        "schedule": crontab(**outpost_service_connection_monitor_period),
        "options": {"queue": "authentik_scheduled"},
    },
    "outpost_token_ensurer": {
        "task": "authentik.outposts.tasks.outpost_token_ensurer",
        "schedule": crontab(**outpost_token_ensurer_period),
        "options": {"queue": "authentik_scheduled"},
    },
    "outpost_connection_discovery": {
        "task": "authentik.outposts.tasks.outpost_connection_discovery",
        "schedule": crontab(**outpost_connection_discovery_period),
        "options": {"queue": "authentik_scheduled"},
    },
}
