from fastapi import APIRouter, Depends
from com.jinmini.utils.creational.builder.db_builder import get_db
from com.jinmini.accoount.guest.manager.web.manager_controller import ManagerController

router = APIRouter()
controller = ManagerController()

@router.post(path="/manager/create")
async def create_manager():
    return controller.hello_manager()

@router.get(path="/manager/detail")
async def get_manager_detail():
    return controller.hello_manager()

@router.get("/manager/list")
async def get_manager_list(db=Depends(get_db)):
    return controller.get_manager_list()

@router.put(path="/manager/update")
async def update_manager():
    return controller.hello_manager()

@router.delete(path="/manager/delete")
async def delete_manager():
    return controller.hello_manager()


