import pytest
from config.db import create_db_session
from config.uuid import generate_id
from companies.models import Company
from companies.repositories import CompanyRepository
from tests.util.testcontainer import create_postgres_container
from tests.util.alembic import run_migrations


@pytest.fixture()
def db_session():
    """Returns a new PortablePostgresContainer instance"""
    postgres = create_postgres_container(
        db_name="worklet",
        db_username="postgres",
        db_password="postgres",
        db_port="5432"
    )
    postgres.start()
    db_uri = postgres.get_connection_url()
    db_session = create_db_session(db_uri)
    run_migrations(db_uri)
    yield db_session
    postgres.stop()


def test_list_none_companies(db_session):
    repository = CompanyRepository(db_session)
    result = repository.list_all()

    assert len(result) == 0


def test_list_all_companies(db_session):
    repository = CompanyRepository(db_session)
    repository.save(Company(id=generate_id(), name="Pepsi"))
    result = repository.list_all()

    assert len(result) == 1
