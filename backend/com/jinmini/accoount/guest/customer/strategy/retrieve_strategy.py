from com.jinmini.accoount.guest.customer.service.retrieve_service import RetrieveCustomerService
from sqlalchemy.orm import Session

class GetallStrategy(RetrieveCustomerService):
    
    async def retrieve(self, db: Session, **kwargs):
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

class GetDetailStrategy(RetrieveCustomerService):

    def retrieve(self, db: Session, **kwargs):
        pass



