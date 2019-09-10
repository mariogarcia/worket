from alembic.config import Config
from alembic import command
from config.logging import log


def run_migrations(db_uri):
    """
    Used to run migrations on-demand by tests
    """
    alembic_cfg = Config()
    alembic_cfg.set_main_option("sqlalchemy.url", db_uri)
    alembic_cfg.set_main_option("script_location", "migrations")

    log.msg('test/util/alembic', db_uri=db_uri)
    command.upgrade(alembic_cfg, "")
    log.msg('test/util/alembic/done')
