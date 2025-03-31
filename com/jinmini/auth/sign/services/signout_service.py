from com.jinmini.utils.config.redis.redis_client import redis_client, delete_token_from_redis

class SignoutService:
    async def handle(self, **kwargs):
        user_id = kwargs.get("user_id")
        authorization = kwargs.get("authorization")
        
        if not user_id:
            return {
                "success": False,
                "message": "사용자 ID가 필요합니다."
            }
        
        # Redis에서 리프레시 토큰 삭제
        success, message = await delete_token_from_redis(redis_client, user_id)
        
        if not success:
            return {
                "success": False,
                "message": f"로그아웃 중 오류가 발생했습니다: {message}"
            }
        
        return {
            "success": True,
            "message": "로그아웃 되었습니다."
        }

