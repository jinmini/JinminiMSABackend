from starlette.responses import JSONResponse
from fastapi import APIRouter, Body, Depends
from backend.com.jinmini.accoount.common.user.model.user_schema import UserSchema
from backend.com.jinmini.auth.sign.api.auth_controller import AuthController
from backend.com.jinmini.auth.sign.models.auth_schema import AuthSchema
from sqlalchemy.ext.asyncio import AsyncSession
from backend.com.jinmini.utils.creational.builder.db_builder import get_db

router = APIRouter()
controller = AuthController()

@router.post("/signin", response_model=AuthSchema)
async def handle_signin(user_schema: UserSchema = Body(UserSchema()),
                        db: AsyncSession = Depends(get_db)):
    
    result = await controller.signin(user_schema, db)

    return JSONResponse(content={"message": "", "result": ""})
