from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text
from com.jinmini.utils.creational.abstract.abstract_service import AbstractService

class GetAllRepository(AbstractService):

    async def handle(self, db, **kwargs):
        return await self.retrieve(db, **kwargs)

    async def retrieve(self, db, **kwargs):
        print("💯🌈 GetAllRepository 로 진입함:")
        query = "SELECT * FROM member"
        try:
            # AsyncDatabase 클래스의 fetch 메서드 직접 사용
            records = await db.fetch(query)
            print("💯🌈 데이터 조회 결과:", records)
            
            # asyncpg의 Record 객체를 딕셔너리로 변환
            customers = [
                {
                    "id": record["user_id"],
                    "email": record["email"],
                    "name": record["name"]
                }
                for record in records
            ]
            
            return customers
        except Exception as e:
            print("⚠️ 데이터 조회 중 오류 발생:", str(e))
            return {"error": "데이터 조회 중 오류가 발생했습니다."}
  

class GetDetailRepository(AbstractService):

    async def handle(self, db, **kwargs):
        user_id = kwargs.get("user_id")
        if not user_id:
            return {"error": "user_id is required"}
        return await self.retrieve(db, user_id)

    async def retrieve(self, db, user_id: str):
        # 상세 조회 로직 구현
        query = "SELECT * FROM member WHERE user_id = $1"
        try:
            # AsyncDatabase 클래스의 fetch 메서드 직접 사용
            records = await db.fetch(query, user_id)
            
            if not records:
                return {"error": "User not found"}
                
            record = records[0]
            return {
                "id": record["user_id"],
                "email": record["email"],
                "name": record["name"]
            }
        except Exception as e:
            print("⚠️ 데이터 조회 중 오류 발생:", str(e))
            return {"error": "데이터 조회 중 오류가 발생했습니다."}
