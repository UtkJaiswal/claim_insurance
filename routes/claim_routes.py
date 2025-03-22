from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from schemas.claim import ClaimCreate, ClaimResponse
from services.claim_service import create_claim, get_claims_by_customer
from typing import List

router = APIRouter()

@router.post("/", response_model=ClaimResponse)
def create_new_claim(claim: ClaimCreate, db: Session = Depends(get_db)):
    return create_claim(db, claim)

@router.get("/{customer_id}/claims", response_model=List[ClaimResponse])
def get_all_claims_by_customer(customer_id: int, db: Session = Depends(get_db)):
    claims = get_claims_by_customer(db, customer_id)
    if not claims:
        raise HTTPException(status_code=404, detail="No claims found")
    return claims
