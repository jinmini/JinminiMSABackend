from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from com.jinmini.accoount.guest.customer.models.customer_entity import CustomerEntity
from com.jinmini.accoount.guest.customer.repositories.create_customer import CustomerRepository

class SignupService:

    async def handle(self, **kwargs):
        user_schema = kwargs.get("user_schema")
        db = kwargs.get("db")

        # 사용자 id 중복 검사
        query = select(CustomerEntity).filter(CustomerEntity.user_id == user_schema.user_id)
        result = await db.execute(query)
        existing_user = result.scalar_one_or_none()

        if existing_user:
            return {
                "success": False,
                "message": "이미 존재하는 사용자입니다."
            }
        
        # 사용자 생성
        try:
            customer_repo = CustomerRepository()
            new_customer = await customer_repo.create_customer(db, user_schema)

            return {
                "success": True,
                "message": "회원가입 성공",
                "user_id": new_customer.user_id
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"회원가입 실패: {str(e)}"
            }
