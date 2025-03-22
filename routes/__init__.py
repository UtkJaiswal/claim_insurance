from fastapi import APIRouter
from .customer_routes import router as customer_router
from .claim_routes import router as claim_router

router = APIRouter()
router.include_router(customer_router, prefix="/customers", tags=["Customers"])
router.include_router(claim_router, prefix="/claims", tags=["Claims"])
