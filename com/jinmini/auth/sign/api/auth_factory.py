from backend.com.jinmini.auth.sign.models.auth_action import AuthAction

class AuthFactory:
    
    strategy_map = {
        AuthAction.SIGN_IN: signin(),
        AuthAction.SIGN_OUT: signout(),
        AuthAction.FORGET_PASSWORD: forget_password(),
        AuthAction.RESET_PASSWORD: reset_password(),
    }

    @staticmethod
    async def create(strategy, **kwargs):
        instance = AuthFactory.strategy_map[strategy]
        if not instance:
            raise Exception(f"Invalid strategy: {strategy}")
        return await instance.handle(**kwargs)

