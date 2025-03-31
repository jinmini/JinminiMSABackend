from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv

# .env 로드
load_dotenv()

# 환경변수에서 값 읽기
SECRET_KEY = os.getenv("SECRET_KEY")
REFRESH_SECRET_KEY = os.getenv("REFRESH_SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 15))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", 7))


def create_access_token(user_dict: dict) -> str:
    issued_at = datetime.now(timezone.utc)
    expire = issued_at + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    payload = {
        "sub": user_dict.get("user_id"),
        "name": user_dict.get("name"),
        "iat": int(issued_at.timestamp()),
        "exp": int(expire.timestamp())
    }

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def create_refresh_token(user_dict: dict) -> str:
    issued_at = datetime.now(timezone.utc)
    expire = issued_at + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)

    payload = {
        "sub": user_dict.get("user_id"),
        "name": user_dict.get("name"),
        "iat": int(issued_at.timestamp()),
        "exp": int(expire.timestamp())
    }

    return jwt.encode(payload, REFRESH_SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token: str, secret_key: str = SECRET_KEY) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {"payload": payload, "valid": True}
    except JWTError:
        return {"payload": None, "valid": False}
