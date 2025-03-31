from com.jinmini.accoount.guest.customer.models.customer_entity import CustomerEntity
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from com.jinmini.utils.config.security.password_utils import get_password_hash

class CustomerRepository:

    @staticmethod
    async def create_customer(db : AsyncSession, customer_data: dict):
        # 비밀번호 해시 처리 - 테스트를 위해 주석 처리
        # if hasattr(customer_data, 'password'):
        #     customer_data.password = get_password_hash(customer_data.password)
        # elif isinstance(customer_data, dict) and 'password' in customer_data:
        #     customer_data['password'] = get_password_hash(customer_data['password'])
            
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

    
 