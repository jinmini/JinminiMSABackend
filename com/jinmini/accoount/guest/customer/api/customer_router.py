from pydantic import BaseModel, EmailStr, Field
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException
from com.jinmini.accoount.guest.customer.api.customer_controller import CustomerController
from com.jinmini.accoount.guest.customer.models.customer_schema import CustomerSchema
from com.jinmini.utils.creational.builder.db_builder import get_db
from typing import List, Optional
from sqlalchemy import select
from com.jinmini.accoount.guest.customer.models.customer_entity import CustomerEntity

router = APIRouter()
controller = CustomerController()

class CustomerResponse(BaseModel):
    """고객 응답 모델"""
    user_id: str
    email: EmailStr
    name: str

class CustomerListResponse(BaseModel):
    """고객 목록 응답 모델"""
    customers: List[CustomerResponse]

@router.post(path="/create", response_model=CustomerResponse, status_code=201)
async def create_customer(
    new_customer: CustomerSchema, 
    db: AsyncSession = Depends(get_db)
):
    
    try:
        return await controller.create_customer(db=db, new_customer=new_customer)
    except Exception as e:
        print(f"고객 생성 중 오류 발생: {e}")
        raise HTTPException(status_code=500, detail="고객 생성 중 오류가 발생했습니다.")

@router.get(path="/detail", response_model=CustomerResponse)
async def get_customer_detail(user_id: str, db: AsyncSession = Depends(get_db)):
    
    try:
        customer = await controller.get_customer_by_id(db=db, user_id=user_id)
        if not customer:
            raise HTTPException(status_code=404, detail="고객을 찾을 수 없습니다.")
        return customer
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"고객 조회 중 오류 발생: {e}")
        raise HTTPException(status_code=500, detail="고객 조회 중 오류가 발생했습니다.")

@router.get("/list", response_model=CustomerListResponse)
async def get_customer_list(db: AsyncSession = Depends(get_db)):
    
    try:
        customers = await controller.get_all_customers(db=db)
        return {"customers": customers}
    except Exception as e:
        print(f"고객 목록 조회 중 오류 발생: {e}")
        raise HTTPException(status_code=500, detail="고객 목록 조회 중 오류가 발생했습니다.")

@router.put(path="/update", response_model=CustomerResponse)
async def update_customer(updated_customer: CustomerSchema, db: AsyncSession = Depends(get_db)):
    
    try:
        customer = await controller.update_customer(db=db, updated_customer=updated_customer)
        if not customer:
            raise HTTPException(status_code=404, detail="고객을 찾을 수 없습니다.")
        return customer
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"고객 정보 업데이트 중 오류 발생: {e}")
        raise HTTPException(status_code=500, detail="고객 정보 업데이트 중 오류가 발생했습니다.")

@router.delete(path="/delete", status_code=204)
async def delete_customer(user_id: str, db: AsyncSession = Depends(get_db)):
    
    try:
        success = await controller.delete_customer(db=db, user_id=user_id)
        if not success:
            raise HTTPException(status_code=404, detail="고객을 찾을 수 없습니다.")
        return None
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"고객 삭제 중 오류 발생: {e}")
        raise HTTPException(status_code=500, detail="고객 삭제 중 오류가 발생했습니다.")


