from sqlalchemy import create_engine
from sqlalchemy.orm import (scoped_session, sessionmaker)
from sqlalchemy.ext.declarative import declarative_base
from config.yaml import config


def create_db_uri():
    return "".format()


def create_db_session(uri):
    """
    Creates a new SQLAlchemy session
    """
    engine = create_engine(uri)
    session = scoped_session(
        sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=engine
        )
    )
    return session


Base = declarative_base()
db_session = create_db_session(config.database.url)

# We will need this for querying
Base.query = db_session.query_property()
