from backend.com.jinmini.auth.sign.api.auth_factory import AuthFactory
from backend.com.jinmini.auth.sign.models.auth_action import AuthAction


class AuthController:

    def __init__(self):
        pass

    async def signin(self, **kwargs):
        return await AuthFactory.create(AuthAction.SIGN_IN, **kwargs)

    async def signout(self, **kwargs):
        return await AuthFactory.create(AuthAction.SIGN_OUT, **kwargs)
    
    async def forget_password(self, **kwargs):
        return await AuthFactory.create(AuthAction.FORGET_PASSWORD, **kwargs)

