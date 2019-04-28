from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Customer(Base):
    __tablename__ = "customer"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    email = Column(String)
    created = Column(DateTime)
    verified = Column(Boolean)

    def __repr__(self):
        return f"<{self.__class__.__name__}(Id={self.id}, Email={self.email})>"
