from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession

class DeleteManagerService(ABC):
    
    @abstractmethod
    async def delete(self, db: AsyncSession, manager_id: int):
        pass

