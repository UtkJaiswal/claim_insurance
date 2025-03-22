from pydantic import BaseModel
from typing import List

class ClaimBase(BaseModel):
    customer_id: int
    policy_id: int

class ClaimCreate(ClaimBase):
    pass

class ClaimResponse(ClaimBase):
    id: int

    class Config:
        orm_mode = True
