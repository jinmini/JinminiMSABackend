from starlette.responses import JSONResponse
from fastapi import APIRouter, Body, Depends, Header
from com.jinmini.accoount.common.user.model.user_schema import UserSchema
from com.jinmini.auth.sign.api.auth_controller import AuthController
from com.jinmini.auth.sign.models.auth_schema import AuthSchema, SigninSchema, SigninResponseSchema
from sqlalchemy.ext.asyncio import AsyncSession
from com.jinmini.utils.creational.builder.db_builder import get_db
from typing import Optional

router = APIRouter()
controller = AuthController()

@router.post("/signin", response_model=SigninResponseSchema)
async def handle_signin(login_schema: SigninSchema = Body(...),
                        db: AsyncSession = Depends(get_db)):
    
    result = await controller.signin(login_schema=login_schema, db=db)

    return JSONResponse(content=result) 

@router.post("/signup", response_model=AuthSchema)
async def handle_signup(user_schema: UserSchema = Body(...), #Body 파라미터는 요청 본문에서 데이터를 가져오는 데 사용, Request Body에 있는 데이터를 파싱하여 파라미터로 전달
                        db: AsyncSession = Depends(get_db)):
    
    result = await controller.signup(user_schema=user_schema, db=db)

    return JSONResponse(content=result) 

@router.post("/signout")
async def handle_signout(user_id: str = Body(...), 
                         authorization: Optional[str] = Header(None),
                         db: AsyncSession = Depends(get_db)):
    
    result = await controller.signout(user_id=user_id, authorization=authorization, db=db)
    
    return JSONResponse(content=result)

