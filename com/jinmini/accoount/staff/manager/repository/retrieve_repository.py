from com.jinmini.accoount.staff.manager.model.manager_entity import ManagerEntity
from sqlalchemy.ext.asyncio import AsyncSession

class RetrieveRepository:
    
    def __init__(self):
        pass

    async def get_all_managers(self, db: AsyncSession):

        result = db.query(ManagerEntity).all()
        return result


