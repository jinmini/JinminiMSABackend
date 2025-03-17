from com.jinmini.accoount.staff.manager.model.manager_schema import ManagerSchema
from com.jinmini.accoount.staff.manager.service.create_service import CreateManagerService
from sqlalchemy.ext.asyncio import AsyncSession

class DefaultCreateManagerRepository(CreateManagerService):
    
    async def create(self, db: AsyncSession, new_manager: ManagerSchema):
        await db.add(ManagerEntity(
            user_id=new_manager.user_id,
            name=new_manager.name,
            email=new_manager.email,
            password=new_manager.password,
        ))

        await db.commit()
        await db.refresh(new_manager)
        return new_manager

class ValidatedCreateManagerRepository(CreateManagerService):
    
    async def create(self, db: AsyncSession, new_manager: ManagerSchema):
        pass



