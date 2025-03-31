import redis.asyncio as redis
import os
from typing import Optional, Tuple

# Redis 연결 설정을 환경 변수에서 가져옵니다
redis_host = os.getenv("REDIS_HOST", "redis")  # 기본값을 'redis'로 변경
redis_port = int(os.getenv("REDIS_PORT", 6379))
redis_password = os.getenv("REDIS_PASSWORD", None)
redis_db = int(os.getenv("REDIS_DB", 0))
redis_url = os.getenv("REDIS_URL", None)

# Redis 클라이언트 초기화 - URL 또는 개별 파라미터 사용
if redis_url:
    # URL이 제공된 경우 URL로 연결
    try:
        redis_client = redis.from_url(redis_url, decode_responses=True)
        print(f"Redis URL 사용하여 연결: {redis_url}")
    except Exception as e:
        print(f"Redis URL 연결 실패, 개별 파라미터로 시도합니다: {str(e)}")
        redis_client = redis.Redis(
            host=redis_host, 
            port=redis_port, 
            password=redis_password,
            db=redis_db,
            decode_responses=True
        )
else:
    # 개별 파라미터로 연결
    redis_client = redis.Redis(
        host=redis_host, 
        port=redis_port, 
        password=redis_password,
        db=redis_db,
        decode_responses=True
    )
    print(f"Redis 개별 파라미터 사용하여 연결: {redis_host}:{redis_port}")

async def save_token_to_redis(redis_client, token: str, user_id: str, expires_in: int = 60*60*24*7) -> Tuple[bool, str]:
    """
    Redis에 리프레시 토큰을 저장하고 저장 결과를 확인합니다.
    
    Args:
        redis_client: Redis 클라이언트 인스턴스
        token: 저장할 토큰
        user_id: 사용자 ID
        expires_in: 만료 시간(초)
    
    Returns:
        Tuple[bool, str]: (성공 여부, 메시지)
    """
    try:
        # 토큰 저장
        await redis_client.set(f"refresh:{user_id}", token, ex=expires_in)
        
        # 저장된 토큰 확인
        stored_token = await redis_client.get(f"refresh:{user_id}")
        if stored_token == token:
            return True, "토큰이 성공적으로 저장되었습니다."
        else:
            return False, "토큰 저장 확인에 실패했습니다."
            
    except redis.RedisError as e:
        return False, f"Redis 오류: {str(e)}"
    except Exception as e:
        return False, f"예상치 못한 오류: {str(e)}"

async def get_token_from_redis(redis_client, user_id: str) -> Optional[str]:
    """
    Redis에서 사용자의 리프레시 토큰을 조회합니다.
    
    Args:
        redis_client: Redis 클라이언트 인스턴스
        user_id: 사용자 ID
    
    Returns:
        Optional[str]: 토큰이 존재하면 토큰 값, 없으면 None
    """
    try:
        return await redis_client.get(f"refresh:{user_id}")
    except:
        return None

async def delete_token_from_redis(redis_client, user_id: str) -> Tuple[bool, str]:
    """
    Redis에서 사용자의 리프레시 토큰을 삭제합니다.
    
    Args:
        redis_client: Redis 클라이언트 인스턴스
        user_id: 사용자 ID
    
    Returns:
        Tuple[bool, str]: (성공 여부, 메시지)
    """
    try:
        # 토큰 삭제 전 존재 여부 확인
        token_exists = await redis_client.exists(f"refresh:{user_id}")
        
        if token_exists:
            # 토큰 삭제
            await redis_client.delete(f"refresh:{user_id}")
            
            # 삭제 확인
            token_deleted = not await redis_client.exists(f"refresh:{user_id}")
            
            if token_deleted:
                return True, "토큰이 성공적으로 삭제되었습니다."
            else:
                return False, "토큰 삭제 확인에 실패했습니다."
        else:
            return True, "삭제할 토큰이 존재하지 않습니다."
            
    except redis.RedisError as e:
        return False, f"Redis 오류: {str(e)}"
    except Exception as e:
        return False, f"예상치 못한 오류: {str(e)}"
