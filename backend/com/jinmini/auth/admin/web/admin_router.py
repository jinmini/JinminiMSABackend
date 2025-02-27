from fastapi import APIRouter
from com.jinmini.auth.admin.web.admin_controller import AdminController
from com.jinmini.auth.user.service.add_user import AddUser

router = APIRouter()
add_user = AddUser()
controller = AdminController()

@router.get(path="/")
async def admin_user():
    return controller.admin_user()   

def add_user(slef, admin):
    print(f"컨트롤러1➕사용자 추가 : {admin}")
    return 

def gest_user(slef, admin):
    print(f"컨트롤러2➕사용자 조회회 : {admin}")
    return 

def update(slef, admin):
    print(f"컨트롤러3사용자 수정정 : {admin}")
    return 

def delete(slef, admin):
    print(f"컨트롤러1➕사용자 삭제제 : {admin}")
    return "success"    