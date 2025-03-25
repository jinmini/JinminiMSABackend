from com.jinmini.utils.creational.abstract.abstract_service import AbstractService
from sqlalchemy.ext.asyncio import AsyncSession
from com.jinmini.accoount.guest.customer.models.customer_schema import CustomerSchema

class UpdateCustomer(AbstractService):

    async def handle(self, db: AsyncSession, update_customer: CustomerSchema):
        pass

class PatchCustomer(AbstractService):

    async def handle(self, db: AsyncSession, update_customer: CustomerSchema):
        pass
