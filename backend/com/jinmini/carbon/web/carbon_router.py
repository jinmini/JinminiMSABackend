from fastapi import APIRouter
from com.jinmini.carbon.service.add_carbon import AddCarbon
from com.jinmini.carbon.web.carbon_controller import CarbonController

router = APIRouter()
add_carbon = AddCarbon()
controller = CarbonController()

@router.get(path="/")
async def carbon_user():
    return controller.carbon_user()

def add_user(slef, user):
    print(f"컨트롤러1➕사용자 추가 : {user}")

    return 

def gest_user(slef, user):
    print(f"컨트롤러2➕사용자 조회회 : {user}")
    return 

def update(slef, user):
    print(f"컨트롤러3사용자 수정정 : {user}")
    return 

def delete(slef, user):
    print(f"컨트롤러1➕사용자 삭제제 : {user}")
    return "success"    