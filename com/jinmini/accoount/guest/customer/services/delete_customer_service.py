from sqlalchemy.ext.asyncio import AsyncSession
from com.jinmini.utils.creational.abstract.abstract_service import AbstractService

class DeleteCustomer(AbstractService):
    
    async def handle(self, db: AsyncSession, user_id: int):
        pass

class RemoveCustomer(AbstractService):
    
    async def handle(self, db: AsyncSession, user_id: int):
        pass
