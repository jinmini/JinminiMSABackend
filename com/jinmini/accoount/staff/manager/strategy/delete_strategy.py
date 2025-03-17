from com.jinmini.accoount.staff.manager.service.delete_service import DeleteManagerService
from sqlalchemy.ext.asyncio import AsyncSession

class SoftDeleteManagerStrategy(DeleteManagerService):

    async def delete(self, db: AsyncSession, manager_id: int):
        pass

class HardDeleteManagerStrategy(DeleteManagerService):

    async def delete(self, db: AsyncSession, manager_id: int):
        pass


