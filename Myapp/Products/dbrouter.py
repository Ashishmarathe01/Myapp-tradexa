from .models import Product

class PRouter(object):

    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label == 'Products':
            return 'product_db'
        return 'default'

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label == 'Products':
            return 'product_db'
        return 'default'



    