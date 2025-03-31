from com.jinmini.utils.config.redis.redis_client import redis_client
from datetime import timedelta

async def store_refresh_token(user_id: str, token: str, expires_in: int = 60*60*24*7):
    await redis_client.set(f"refresh:{user_id}", token, ex=expires_in)

async def verify_refresh_token(user_id: str, token: str) -> bool:
    stored = await redis_client.get(f"refresh:{user_id}")
    return stored == token

async def invalidate_refresh_token(user_id: str):
    await redis_client.delete(f"refresh:{user_id}")