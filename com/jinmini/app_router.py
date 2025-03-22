from fastapi import APIRouter
from com.jinmini.accoount.account_router import router as account_router
from com.jinmini.auth.api.auth_router import router as auth_router

router = APIRouter()

router.include_router(account_router)
router.include_router(auth_router, prefix="/auth")

