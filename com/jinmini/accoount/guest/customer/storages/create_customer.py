from com.jinmini.accoount.guest.customer.models.customer_entity import CustomerEntity
from sqlalchemy.ext.asyncio import AsyncSession
from com.jinmini.accoount.guest.customer.models.customer_schema import CustomerSchema

async def create_customer(db: AsyncSession, new_customer: CustomerSchema):
    return CustomerEntity(
        user_id = new_customer.user_id,
        name = new_customer.name,
        email = new_customer.email,
        password = new_customer.password
    )

