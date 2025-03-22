from com.jinmini.accoount.guest.customer.models.customer_entity import CustomerEntity
from com.jinmini.accoount.guest.customer.models.customer_schema import CustomerSchema
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Union, Any

async def create_customer(db: Any, new_customer: CustomerSchema):
    # 고객 엔티티 생성
    customer_entity = CustomerEntity(
        user_id=new_customer.user_id,
        name=new_customer.name,
        email=new_customer.email,
        password=new_customer.password
    )
    
    # db 객체 타입에 따라 다르게 처리
    if isinstance(db, AsyncSession):
        # SQLAlchemy 세션 사용
        print("SQLAlchemy AsyncSession 사용")
        db.add(customer_entity)
    else:
        # AsyncDatabase 사용 (직접 SQL 실행)
        print("AsyncDatabase 사용 - SQL 직접 실행")
        query = """
        INSERT INTO member (user_id, email, name, password)
        VALUES ($1, $2, $3, $4)
        """
        try:
            await db.execute(
                query,
                new_customer.user_id,
                new_customer.email,
                new_customer.name,
                new_customer.password
            )
        except Exception as e:
            print(f"SQL 실행 오류: {e}")
            raise e
    
    return customer_entity
