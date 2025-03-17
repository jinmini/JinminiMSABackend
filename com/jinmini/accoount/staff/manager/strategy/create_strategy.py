from com.jinmini.accoount.staff.manager.model.manager_schema import ManagerSchema
from com.jinmini.accoount.staff.manager.service.create_service import CreateManagerService
from sqlalchemy.ext.asyncio import AsyncSession

class DefaultCreateManagerStrategy(CreateManagerService):   

    async def create(self, db: AsyncSession, new_manager: ManagerSchema):
        pass
    
class ValidatedCreateManagerStrategy(CreateManagerService):

    async def create(self, db: AsyncSession, new_manager: ManagerSchema):
        pass
