from com.jinmini.auth.sign.models.auth_action import AuthAction
from com.jinmini.auth.sign.services.signin_service import SigninService
from com.jinmini.auth.sign.services.signout_service import SignoutService
from com.jinmini.auth.sign.services.signup_service import SignupService

class AuthFactory:
    
    strategy_map = {
        AuthAction.SIGN_IN: SigninService(),
        AuthAction.SIGN_OUT: SignoutService(),
        AuthAction.SIGN_UP: SignupService(),
    }

    @staticmethod
    async def create(strategy, **kwargs):
        instance = AuthFactory.strategy_map[strategy]
        if not instance:
            raise Exception(f"Invalid strategy: {strategy}")
        return await instance.handle(**kwargs)

