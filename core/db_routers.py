# core/db_routers.py

class MaritimeRouter:
    """
    A router to control all database operations on models in the
    maritime application.
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'maritime':
            return 'maritime'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'maritime':
            return 'maritime'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        # Allow any relation if both models are in the maritime app
        if obj1._meta.app_label == 'maritime' and obj2._meta.app_label == 'maritime':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'maritime':
            # Only allow migrations on the maritime database for maritime app models.
            return db == 'maritime'
        return None


class WeatherRouter:
    """
    A router to control all database operations on models in the
    weather application.
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'weather':
            return 'weather'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'weather':
            return 'weather'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'weather' and obj2._meta.app_label == 'weather':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'weather':
            # Migrations for weather app should run on the weather database.
            return db == 'weather'
        return None
