from conf import database


class CheckerRouter:
    def __init__(self):
        self.model_list = ['default'] + [name for name in database.DATABASE_NAMES.keys()]

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.model_list:
            return model._meta.app_label
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.model_list:
            return model._meta.app_label
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return None