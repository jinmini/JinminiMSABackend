from com.jinmini.accoount.staff.manager.service.update_service import UpdateManagerService
from sqlalchemy.ext.asyncio import AsyncSession
from com.jinmini.accoount.staff.manager.model.manager_schema import ManagerSchema

class FullUpdateManagerStrategy(UpdateManagerService):
    
    async def update(self, db: AsyncSession, manager_id: int, manager: ManagerSchema):
        pass

class PartialUpdateManagerStrategy(UpdateManagerService):
    
    async def update(self, db: AsyncSession, manager_id: int, manager: ManagerSchema):
        pass

