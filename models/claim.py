from sqlalchemy import Column, Integer, ForeignKey
from config.database import Base
from sqlalchemy.orm import relationship

class Claim(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    policy_id = Column(Integer, nullable=False)

    customer = relationship("Customer", back_populates="claims")
