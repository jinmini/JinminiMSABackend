from fastapi import APIRouter
from com.jinmini.accoount.guest.customer.web.customer_router import router as customer_router

router = APIRouter()

router.include_router(customer_router, prefix="/customer")