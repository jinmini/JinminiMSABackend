from fastapi import APIRouter
from com.jinmini.auth.admin.admin_service import AdminService

router = APIRouter()
admin_service = AdminService()

@router.get("/")
def hello():
    return admin_service.hello()  

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