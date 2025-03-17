from fastapi import APIRouter
from com.jinmini.accoount.account_router import router as account_router

router = APIRouter()

router.include_router(account_router)

