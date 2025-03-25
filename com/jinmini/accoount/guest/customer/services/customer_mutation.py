from sqlalchemy.ext.asyncio import AsyncSession
from com.jinmini.utils.creational.abstract.abstract_service import AbstractService

class CreateCustomer(AbstractService):

    async def handle(self, db: AsyncSession, **kwargs):
        pass


