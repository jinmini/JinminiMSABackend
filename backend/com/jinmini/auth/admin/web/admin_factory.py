from com.jinmini.auth.admin.service.admin_user import AdminUser

strategy_map = {
    "admin_user": AdminUser(),
}
class AdminFactory:

    @staticmethod
    def create(strategy, **kwargs):
        instance = strategy_map[strategy]
        if not instance:
            raise Exception("invalid strategy")
        return instance.handle(**kwargs)
