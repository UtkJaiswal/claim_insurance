from pydantic import BaseModel
from typing import List

class CustomerBase(BaseModel):
    name: str
    phone: str
    email: str
    aadhar_number: str
    pan_number: str
    

class CustomerCreate(CustomerBase):
    pass

class CustomerResponse(CustomerBase):
    id: int

    class Config:
        orm_mode = True
