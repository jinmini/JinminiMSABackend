from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 비밀번호 해시화 (signup 시 사용)
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# 비밀번호 검증 (signin 시 사용)
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)