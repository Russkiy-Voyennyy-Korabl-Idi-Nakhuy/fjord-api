from pydantic import BaseSettings


class AppEnvTypes:
    """
    Available application environments.
    """

    prod = "prod"
    dev = "dev"
    test = "test"


class ProjectEnv:
    """
    Available project environments.
    """

    production = "production"
    staging = "staging"
    testing = "testing"


class BaseAppSettings(BaseSettings):
    """
    Base application setting class.
    """

    current_env: str

    app_env: str = AppEnvTypes.prod

    # Redis setup.
    redis_host: str
    redis_port: int
    redis_password: str
    redis_key: str = "v-proxies:universal"

    # Mongo env variables.
    mongo_host: str
    mongo_port: int
    mongo_db: str
    mongo_user: str | None
    mongo_password: str | None
    mongo_auth_source: str | None
    mongo_tasks_collection: str

    # Translation providers secrets
    deepl_auth_key: str | None = None
    libre_api_key: str | None = None
    mymemory_email: str | None = None
    detect_language_api_key: str

    # How many tasks can be processed in parallel.
    max_concurrent_tasks: int

    # Scheduler background task interval.
    scheduler_task_interval: int

    # Flag enable/disable background tasks on startup.
    run_background_tasks: bool

    # Graylog setup.
    graylog_host: str | None
    graylog_input_port: int | None = 0

    # Sentry setup.
    sentry_dsn: str | None

    # Proxy settings
    log_proxies: bool | None = False
    proxy_score_max = 1
    proxy_score_min = 0
    proxy_score_init = 1

    class Config:
        env_file = ".env"