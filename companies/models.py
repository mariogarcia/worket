from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from config.db import Base


class Company(Base):
    __tablename__ = 'companies'
    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String)
