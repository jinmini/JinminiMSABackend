
from fastapi import APIRouter
from com.jinmini.auth.user.user_service import UserService

router = APIRouter()
user_service = UserService()

@router.get("/")
def hello():
    return user_service.hello()  

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