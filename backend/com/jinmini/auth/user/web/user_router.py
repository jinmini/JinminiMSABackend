from fastapi import APIRouter, Depends
from sqlalchemy.sql import text
from sqlalchemy.orm import Session
from com.jinmini.auth.user.service.add_user import AddUser
from com.jinmini.auth.user.web.user_controller import UserController
from database import get_db

router = APIRouter()
add_user = AddUser()
controller = UserController()

@router.get(path="/")
async def hello_user():
    return controller.hello_user()  

@router.get("/db-test")
def db_test(db: Session = Depends(get_db)):
    """PostgreSQL 연결 테스트 및 members 테이블 데이터 가져오기"""
    try:
        query = text("SELECT * FROM members;")  # ✅ text()로 감싸기
        result = db.execute(query).fetchall()
        return {"members": [dict(row._mapping) for row in result]}  # ✅ SQLAlchemy Row 변환
    except Exception as e:
        return {"error": str(e)}

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