"""Cron utilities"""
from structlog.stdlib import get_logger
from authentik.lib.config import CONFIG

def get_task_period(task_name: str, default_period: dict) -> dict:
    """Get Task schedule from env var if present.

    The name of the env var must be {task_name}_period

    ie:
    AUTHENTIK_BLUEPRINTS_DISCOVERY_PERIOD

    The format used is the celery crontab schedules described here:

    https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html#id5

    ie:
    {"hour":7, "minute":30, "day_of_week":1}
    {"minute":"*/5"}

    .env example running tasks just once per day
    AUTHENTIK_BLUEPRINTS_DISCOVERY_PERIOD="hour=8, minute=5"
    AUTHENTIK_CLEAR_FAILED_BLUEPRINTS_PERIOD="hour=9, minute=5"
    AUTHENTIK_CERTIFICATE_DISCOVERY_PERIOD="hour=10, minute=5"
    AUTHENTIK_NOTIFICATION_CLEANUP_PERIOD="hour=11, minute=5"
    AUTHENTIK_OUTPOST_CONTROLLER_ALL_PERIOD="hour=12, minute=5"
    AUTHENTIK_OUTPOST_SERVICE_CONNECTION_MONITOR_PERIOD="hour=13, minute=5"
    AUTHENTIK_OUTPOST_TOKEN_ENSURER_PERIOD="hour=14, minute=5"
    AUTHENTIK_OUTPOST_CONNECTION_DISCOVERY_PERIOD="hour=15, minute=5"
    AUTHENTIK_SAVE_REPUTATION_PERIOD="hour=16, minute=5"
    AUTHENTIK_SCIM_SYNC_ALL_PERIOD="hour=17, minute=5"
    AUTHENTIK_CLEAN_EXPIRED_MODELS_PERIOD="hour=18, minute=5"
    AUTHENTIK_USER_CLEANUP_PERIOD="hour=19, minute=5"
    AUTHENTIK_CHECK_PLEX_TOKEN_ALL_PERIOD="hour=20, minute=5"
    """

    logger = get_logger()

    period = CONFIG.y(f"{task_name}_period")

    if period is None:
        period = default_period
    else:
        period = dict(e.split("=") for e in period.split(", "))

    logger.info(f"{task_name} period: {period}")
    return period
