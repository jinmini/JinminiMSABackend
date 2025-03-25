from enum import Enum

class AuthAction(Enum):
    SIGN_IN = "sign_in" # 로그인
    SIGN_OUT = "sign_out" # 로그아웃

    FORGET_PASSWORD = "forget_password" # 비밀번호 찾기
    
    
