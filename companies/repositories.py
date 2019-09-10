from worket.config.db import db_session
from worket.config.logging import log


def list_all():
    """lists all companies"""
    log.msg('companies/repositories/list_all')
    db_session.list_all()
