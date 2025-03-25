from typing import List
from pydantic import BaseModel, EmailStr
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends
from com.jinmini.accoount.guest.customer.api.customer_controller import CustomerController
from com.jinmini.accoount.guest.customer.models.customer_schema import CustomerSchema
from com.jinmini.utils.creational.builder.db_builder import get_db

router = APIRouter()
controller = CustomerController()

class CustomerResponse(BaseModel): # 단일 고객 응답 모델
    user_id: str
    email: EmailStr
    name: str

class CustomerListResponse(BaseModel): # 고객 목록 응답 모델
    customers: List[CustomerResponse]

@router.post(path="/create")
async def create_customer(new_customer: CustomerSchema, db: AsyncSession = Depends(get_db)):
    print("🔎🔎🖥️고객 생성")
    return await controller.create_customer(db=db, new_customer=new_customer)

@router.get(path="/detail")
async def get_customer_detail(user_id: str, db: AsyncSession = Depends(get_db)):
    return await controller.get_customer_by_id(db=db, user_id=user_id)

@router.get("/list", response_model=CustomerListResponse)
async def get_customer_list(db: AsyncSession = Depends(get_db)):
    print("🔎🔎🖥️고객 목록 조회")
    customers = await controller.get_customer_list(db=db)
    return {"customers": customers}

@router.put(path="/update")
async def update_customer(updated_customer: CustomerSchema, db: AsyncSession = Depends(get_db)):
    return await controller.update_customer(db=db, updated_customer=updated_customer)

@router.delete(path="/delete")
async def delete_customer(user_id: str, db: AsyncSession = Depends(get_db)):
    return await controller.delete_customer(db=db, user_id=user_id)


