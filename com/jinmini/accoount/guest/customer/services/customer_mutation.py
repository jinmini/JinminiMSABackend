from sqlalchemy.ext.asyncio import AsyncSession
from com.jinmini.accoount.guest.customer.repositories.create_customer import CustomerRepository
from com.jinmini.utils.creational.abstract.abstract_service import AbstractService

class CreateCustomer(AbstractService):

    async def handle(self, **kwargs):
        db: AsyncSession = kwargs.get("db")
        new_customer = kwargs.get("new_customer")
        try:

           customer_data = {
              "user_id": new_customer.user_id,
              "email": new_customer.email,
              "name": new_customer.name,
              "password": new_customer.password
           }

           customer = await CustomerRepository.create_customer(db, customer_data)

           await db.commit()

           return {
               "user_id": customer.user_id,
               "email": customer.email,
               "name": customer.name,
               "success": True
           }

        except Exception as e:
            print(f"[ERROR] UserCreate failed: {e}")
            await db.rollback()
            raise e


