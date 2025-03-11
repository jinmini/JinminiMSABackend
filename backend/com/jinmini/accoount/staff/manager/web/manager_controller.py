
class ManagerController:
    
    def __init__(self):
        pass

    def create_manager(self, **kwargs):
        return ManagerFactory.create_manager(strategy="create", **kwargs)

    def get_manager_detail(self, **kwargs):
        return ManagerFactory.get_manager_detail(strategy="read_detail", **kwargs)

    def get_manager_list(self, **kwargs):
        return ManagerFactory.get_manager_list(strategy="read_list", **kwargs)

    def update_manager(self, **kwargs):
        return ManagerFactory.update_manager(strategy="update", **kwargs)

    def delete_manager(self, **kwargs):
        return ManagerFactory.delete_manager(strategy="delete", **kwargs)
