from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from com.jinmini.accoount.guest.customer.models.customer_entity import CustomerEntity
from com.jinmini.utils.creational.abstract.abstract_service import AbstractService

class GetCustomers(AbstractService):
    async def handle(self, **kwargs):
        db: AsyncSession = kwargs.get("db")
        try:
           query = select(CustomerEntity)
           result = await db.execute(query)
           customers = result.scalars().all()

           return [
               {
                   "user_id": customer.user_id,
                   "email": customer.email,
                   "name": customer.name
               }
               for customer in customers
           ]

        except Exception as e:
            print(f"[ERROR] GetCustomers failed: {e}")
            raise e


class GetCustomerById(AbstractService):
    async def handle(self, **kwargs):
        pass


