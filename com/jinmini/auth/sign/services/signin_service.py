from com.jinmini.accoount.guest.customer.models.customer_entity import CustomerEntity
from sqlalchemy import select


class SigninService:

    async def handle(self, **kwargs):
        login_schema = kwargs.get("login_schema")
        db = kwargs.get("db")

        # 1. 이메일로 사용자 조회
        query = select(CustomerEntity).filter(CustomerEntity.email == login_schema.email)
        result = await db.execute(query)
        user = result.scalar_one_or_none()

        # 인증 검증
        if user and user.password == login_schema.password:
            return {
                "success": True,
                "message": "로그인 성공",
                "token": "sample_token",  # 실제 토큰 구현 추가 필요
                "user_id": user.user_id
            }
        else:
            return {
                "success": False,
                "message": "이메일 또는 비밀번호가 잘못되었습니다."
            }