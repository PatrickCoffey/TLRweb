
class ETLRouter(object):
    """
    A router to control all database operations on models in the
    TLR_ETL application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read TLR_ETL models go to etl.
        """
        if model._meta.app_label == 'TLR_ETL':
            return 'etl'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write TLR_ETL models go to etl.
        """
        if model._meta.app_label == 'TLR_ETL':
            return 'etl'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the TLR_ETL app is involved.
        """
        if obj1._meta.app_label == 'TLR_ETL' or obj2._meta.app_label == 'TLR_ETL':
            return True
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        """
        Make sure the TLR_ETL app only appears in the 'etl'
        database.
        """
        if app_label == 'TLR_ETL':
            return db == 'etl'
        return None