from starlette.responses import JSONResponse
from fastapi import APIRouter, Body, Depends
from com.jinmini.accoount.common.user.model.user_schema import UserSchema
from com.jinmini.auth.sign.api.auth_controller import AuthController
from com.jinmini.auth.sign.models.auth_schema import AuthSchema
from sqlalchemy.ext.asyncio import AsyncSession
from com.jinmini.utils.creational.builder.db_builder import get_db

router = APIRouter()
controller = AuthController()

@router.post("/signin", response_model=AuthSchema)
async def handle_signin(user_schema: UserSchema = Body(...),
                        db: AsyncSession = Depends(get_db)):
    
    result = await controller.signin(user_schema=user_schema, db=db)

    return JSONResponse(content=result)

@router.post("/signup", response_model=AuthSchema)
async def handle_signup(user_schema: UserSchema = Body(...),
                        db: AsyncSession = Depends(get_db)):
    
    result = await controller.signup(user_schema=user_schema, db=db)

    return JSONResponse(content=result)
