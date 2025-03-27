from starlette.responses import JSONResponse
from fastapi import APIRouter, Body, Depends
from com.jinmini.accoount.common.user.model.user_schema import UserSchema
from com.jinmini.auth.sign.api.auth_controller import AuthController
from com.jinmini.auth.sign.models.auth_schema import AuthSchema, LoginSchema
from sqlalchemy.ext.asyncio import AsyncSession
from com.jinmini.utils.creational.builder.db_builder import get_db

router = APIRouter()
controller = AuthController()

@router.post("/signin", response_model=AuthSchema)
async def handle_signin(login_schema: LoginSchema = Body(...),
                        db: AsyncSession = Depends(get_db)):
    
    result = await controller.signin(login_schema=login_schema, db=db)

    return JSONResponse(content=result) #result에는 토큰 정보가 들어있음

@router.post("/signup", response_model=AuthSchema)
async def handle_signup(user_schema: UserSchema = Body(...), #Body 파라미터는 요청 본문에서 데이터를 가져오는 데 사용, Request Body에 있는 데이터를 파싱하여 파라미터로 전달
                        db: AsyncSession = Depends(get_db)):
    
    result = await controller.signup(user_schema=user_schema, db=db)

    return JSONResponse(content=result) 
