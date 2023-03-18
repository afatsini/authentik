"""Plex source settings"""
from celery.schedules import crontab

from authentik.lib.utils.time import fqdn_rand

from authentik.lib.utils.cron import get_task_period

check_plex_token_all_period = get_task_period(
    "check_plex_token_all", {'minute': fqdn_rand("check_plex_token"), 'hour':"*/3"}
)

CELERY_BEAT_SCHEDULE = {
    "check_plex_token": {
        "task": "authentik.sources.plex.tasks.check_plex_token_all",
        "schedule": crontab(**check_plex_token_all_period),
        "options": {"queue": "authentik_scheduled"},
    },
}
