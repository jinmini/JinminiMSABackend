from pydantic import BaseModel, EmailStr, Field
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException
from com.jinmini.utils.creational.builder.db_builder import get_db
from typing import List, Optional
from com.jinmini.auth.api.auth_controller import AuthController

router = APIRouter()
controller = AuthController()

class UserResponse(BaseModel):
    """사용자 응답 모델"""
    user_id: str
    email: EmailStr
    name: str

class LoginRequest(BaseModel):
    """로그인 요청 모델"""
    user_id: str
    password: str

class LoginResponse(BaseModel):
    """로그인 응답 모델"""
    success: bool
    message: str
    user: Optional[UserResponse] = None
    
class SignupRequest(BaseModel):
    """회원가입 요청 모델"""
    user_id: str
    name: str
    email: EmailStr
    password: str

@router.post("/login", response_model=LoginResponse)
async def login(login_request: LoginRequest, db: AsyncSession = Depends(get_db)):
    """로그인 처리"""
    result = await controller.login(
        db=db, 
        user_id=login_request.user_id, 
        password=login_request.password
    )
    return result

@router.post("/signup", response_model=UserResponse, status_code=201)
async def signup(signup_request: SignupRequest, db: AsyncSession = Depends(get_db)):
    """회원가입 처리"""
    user_data = {
        "user_id": signup_request.user_id,
        "name": signup_request.name,
        "email": signup_request.email,
        "password": signup_request.password
    }
    return await controller.signup(db=db, user_data=user_data) 