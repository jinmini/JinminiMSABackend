from fastapi import APIRouter, Depends
from com.jinmini.accoount.staff.manager.model.manager_schema import ManagerSchema
from com.jinmini.utils.creational.builder.db_builder import get_db
from com.jinmini.accoount.staff.manager.web.manager_controller import ManagerController
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()
controller = ManagerController()

@router.post(path="/create")
async def create_manager(new_manager: ManagerSchema, db: AsyncSession = Depends(get_db)):
    return await controller.hello_manager(db=db, new_manager=new_manager)

@router.get(path="/detail")
async def get_manager_detail(manager_id: int, db: AsyncSession = Depends(get_db)):
    return await controller.hello_manager(db=db, manager_id=manager_id)

@router.get("/list")
async def get_manager_list(db: AsyncSession = Depends(get_db)):
    print("💫💫💫get_manager_list로 진입완료")
    return await controller.get_manager_list(db=db)

@router.put(path="/update")
async def update_manager(manager_id: int, updated_manager: ManagerSchema, db: AsyncSession = Depends(get_db)):
    return await controller.hello_manager(db=db, manager_id=manager_id, updated_manager=updated_manager)

@router.delete(path="/delete")
async def delete_manager(manager_id: int, db: AsyncSession = Depends(get_db)):
    return await controller.hello_manager(db=db, manager_id=manager_id)


