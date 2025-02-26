
class UserService:

    def __init__(self):
        pass

    def hello(self):
        print("Hello World!")
        return{"서비스" : "서비스 호출됨!"}

    def add_user(slef, user):
        print(f"➕사용자 추가 : {user}")
        return user

    def gest_user(slef, user):
        print(f"➕사용자 조회회 : {user}")
        return user
    
    def update(slef, user):
        print(f"➕사용자 수정정 : {user}")
        return user
    
    def delete(slef, user):
        print(f"➕사용자 삭제제 : {user}")
        return "success"
    

