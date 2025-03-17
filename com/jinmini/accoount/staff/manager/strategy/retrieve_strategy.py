from com.jinmini.accoount.staff.manager.service.retrieve_service import RetrieveManagerService
from sqlalchemy.ext.asyncio import AsyncSession

class GetallManagerStrategy(RetrieveManagerService):
    
    async def retrieve(self, db: AsyncSession, **kwargs):
        try:
            query = "SELECT user_id, email, name FROM member"
            result = await db.fetch(query)

            customers = [
                {
                    "id": row["user_id"],
                    "email": row["email"],
                    "name": row["name"]
                }
                for row in result
            ]

            return {"customers": customers, "count": len(customers)}
        except Exception as e:
            print(f"⚠️ 데이터 조회 중 오류 발생:, {str(e)}")
            return {"customers": [], "count": 0, "error": str(e)}

class GetDetailManagerStrategy(RetrieveManagerService):
    
    async def retrieve(self, db: AsyncSession, **kwargs):
        pass
