from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession
from com.jinmini.accoount.staff.manager.model.manager_schema import ManagerSchema

class UpdateManagerService(ABC):

    @abstractmethod
    async def update(self, db: AsyncSession, manager_id: int, manager: ManagerSchema):
        pass
    

