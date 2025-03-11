from fastapi import APIRouter, Depends
from com.jinmini.accoount.guest.customer.web.customer_controller import CustomerController
from com.jinmini.utils.creational.builder.db_builder import get_db

router = APIRouter()
controller = CustomerController()

@router.post(path="/create")
async def create_customer():
    return controller.hello_customer()

@router.get(path="/detail")
async def get_customer_detail():
    return controller.hello_customer()

@router.get("/list")
async def get_customer_list(db=Depends(get_db)):
    print("💫💫💫get_customer_list로 진입완료")
    return await controller.get_customer_list(db=db)

@router.put(path="/update")
async def update_customer():
    return controller.hello_customer()

@router.delete(path="/delete")
async def delete_customer():
    return controller.hello_customer()


