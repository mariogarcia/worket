from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from worket.config.db import Base


class Employee(Base):
    __tablename__ = 'employees'
    uuid = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String)
