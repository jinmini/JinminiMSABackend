from com.jinmini.accoount.guest.customer.models.customer_entity import CustomerEntity
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

class CustomerRepository:

    @staticmethod
    async def create_customer(db : AsyncSession, customer_data: dict):
        
        # 고객 엔티티 생성
        customer_entity = CustomerEntity(**customer_data)
        db.add(customer_entity)
        await db.flush()
        return customer_entity

    @staticmethod
    async def get_all_customers(db: AsyncSession):

        # 모든 고객 조회
        query = select(CustomerEntity)
        result = await db.execute(query)
        return result.scalars().all()

    
 