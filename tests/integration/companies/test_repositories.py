import pytest
from config.db import create_db_session
from config.uuid import generate_id
from companies.models import Company
from companies.repositories import CompanyRepository
from tests.util.testcontainer import create_postgres_container
from tests.util.alembic import run_migrations


@pytest.fixture()
def postgres_container():
    """
    Returns a new PortablePostgresContainer instance
    """
    return create_postgres_container(
        "worklet",
        "postgres",
        "postgres",
        "5432"
    )


def test_list_all_companies(postgres_container):
    with postgres_container as postgres:
        db_uri = postgres.get_connection_url()
        db_session = create_db_session(db_uri)
        repository = CompanyRepository(db_session)

        run_migrations(db_uri)
        repository.save(Company(id=generate_id(), name="Pepsi"))
        result = repository.list_all()

        assert len(result) == 1
