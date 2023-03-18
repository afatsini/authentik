"""LDAP Settings"""
from celery.schedules import crontab

from authentik.lib.utils.time import fqdn_rand

from authentik.lib.utils.cron import get_task_period

ldap_sync_all_period = get_task_period(
    "blueprints_discovery", {"minute": fqdn_rand("sources_ldap_sync"), "hour": "*/2"}
)

CELERY_BEAT_SCHEDULE = {
    "sources_ldap_sync": {
        "task": "authentik.sources.ldap.tasks.ldap_sync_all",
        "schedule": crontab(**ldap_sync_all_period),
        "options": {"queue": "authentik_scheduled"},
    }
}
