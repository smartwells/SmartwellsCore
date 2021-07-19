from .settings import *

DEBUG = True
ALLOWED_HOSTS = ['*']							# разрешаем доступ с любого IP

# добавление тулбара
MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
INSTALLED_APPS.append('debug_toolbar')
INTERNAL_IPS = ('127.0.0.1', 'localhost', '78.25.88.10')
#INTERNAL_IPS = ('192.168.1.1')
