from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession
from com.jinmini.accoount.staff.manager.model.manager_schema import ManagerSchema

class CreateManagerService(ABC):

    @abstractmethod
    async def create(self, db: AsyncSession, new_manager: ManagerSchema):
        pass


