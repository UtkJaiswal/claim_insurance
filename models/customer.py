from sqlalchemy import Column, Integer, String
from config.database import Base
from sqlalchemy.orm import relationship


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    aadhar_number = Column(String, unique=True, nullable=False)
    pan_number = Column(String, unique=True, nullable=False)

    claims = relationship("Claim", back_populates="customer", cascade="all, delete-orphan")

