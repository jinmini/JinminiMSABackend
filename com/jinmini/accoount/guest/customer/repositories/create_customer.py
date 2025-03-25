from com.jinmini.accoount.guest.customer.models.customer_entity import CustomerEntity
from com.jinmini.accoount.guest.customer.models.customer_schema import CustomerSchema
from sqlalchemy.ext.asyncio import AsyncSession

async def create_customer(db: AsyncSession, new_customer: CustomerSchema):
    # 고객 엔티티 생성
    customer_entity = CustomerEntity(
        user_id=new_customer.user_id,
        name=new_customer.name,
        email=new_customer.email,
        password=new_customer.password
    )

    return customer_entity


    
 