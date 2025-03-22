from sqlalchemy.orm import Session
from models.claim import Claim
from schemas.claim import ClaimCreate

def create_claim(db: Session, claim: ClaimCreate):
    db_claim = Claim(**claim.dict())
    db.add(db_claim)
    db.commit()
    db.refresh(db_claim)
    return db_claim

def get_claims_by_customer(db: Session, customer_id: int):
    return db.query(Claim).filter(Claim.customer_id == customer_id).all()
