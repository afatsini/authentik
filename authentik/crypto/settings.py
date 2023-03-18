"""Crypto task Settings"""
from celery.schedules import crontab

from authentik.lib.utils.time import fqdn_rand

from authentik.lib.utils.cron import get_task_period

certificate_discovery_period = get_task_period(
    "certificate_discovery", {'minute': fqdn_rand("crypto_certificate_discovery"), 'hour':"*"}
)
CELERY_BEAT_SCHEDULE = {
    "crypto_certificate_discovery": {
        "task": "authentik.crypto.tasks.certificate_discovery",
        "schedule": crontab(**certificate_discovery_period),
        "options": {"queue": "authentik_scheduled"},
    },
}
