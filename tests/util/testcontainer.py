import os
from config.logging import log
from testcontainers.core.generic import DbContainer


class PortablePostgresContainer(DbContainer):
    """
    Docker container for PostgreSQL database using
    dialect `postgresql+pg8000`
    """
    POSTGRES_USER = os.environ.get("POSTGRES_USER", "test")
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "test")
    POSTGRES_DB = os.environ.get("POSTGRES_DB", "test")

    def __init__(
        self,
        image="postgres:latest",
        db="test",
        user="postgres",
        password="postgres",
        port="5432"
    ):
        super(PortablePostgresContainer, self).__init__(image=image)
        self.port_to_expose = 5432
        self.with_exposed_ports(self.port_to_expose)
        self.POSTGRES_DB = db
        self.POSTGRES_USER = user
        self.POSTGRES_PASSWORD = password

    def _configure(self):
        self.with_env("POSTGRES_USER", self.POSTGRES_USER)
        self.with_env("POSTGRES_PASSWORD", self.POSTGRES_PASSWORD)
        self.with_env("POSTGRES_DB", self.POSTGRES_DB)

    def get_connection_url(self):
        return super()._create_connection_url(dialect="postgresql+pg8000",
                                              username=self.POSTGRES_USER,
                                              password=self.POSTGRES_PASSWORD,
                                              db_name=self.POSTGRES_DB,
                                              port=self.port_to_expose)


def create_postgres_container(db_name, db_username, db_password, db_port):
    """
    Returns a new PortablePostgresContainer instance
    """
    log.msg(
        'testcontainers/create',
        db_name=db_name,
        db_username=db_username,
        db_port=db_port
    )
    return PortablePostgresContainer(
        image="postgres:10-alpine",
        db=db_name,
        user=db_username,
        password=db_password,
        port=db_port
    )
