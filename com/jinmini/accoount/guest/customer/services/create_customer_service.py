from sqlalchemy.ext.asyncio import AsyncSession
from com.jinmini.accoount.guest.customer.models.customer_schema import CustomerSchema
from com.jinmini.accoount.guest.customer.storages.create_customer import create_customer
from com.jinmini.utils.creational.abstract.abstract_service import AbstractService

class CreateCustomer(AbstractService):
    
    async def handle(self, **kwargs):
        db: AsyncSession = kwargs.get("db")
        schema : CustomerSchema = kwargs.get("customer")
        
        try :  
            customer = await create_customer(db, schema)
            db.add(customer)
            await db.commit()
            await db.refresh(customer)
            return customer
        except Exception as e:
            print(f"[ERROR] CustomerCreate failed: {e}")
            await db.rollback()
            raise e
    


