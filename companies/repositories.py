from .models import Company


class CompanyRepository(object):
    def __init__(self, db_session):
        self.db_session = db_session

    def list_all(self):
        """lists all companies"""
        return self.db_session.query(Company).all()

    def save(self, company):
        """saves a new company"""
        self.db_session.add(company)
        self.db_session.commit()
