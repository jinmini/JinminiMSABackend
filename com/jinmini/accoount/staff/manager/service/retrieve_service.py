from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession

class RetrieveManagerService(ABC):

    @abstractmethod
    async def retrieve(self, db: AsyncSession, manager_id: int):
        pass

