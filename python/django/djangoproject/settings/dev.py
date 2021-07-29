from .settings import *

DEBUG = True
ALLOWED_HOSTS = ['*']							# разрешаем доступ с любого IP

# добавление тулбара
MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
INSTALLED_APPS.append('debug_toolbar')
INTERNAL_IPS = ('127.0.0.1', 'localhost', '78.25.88.10', '192.168.1.101')
#INTERNAL_IPS = ('192.168.1.1')

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': '',
        'STATS_FILE': os.path.join(BASE_DIR, 'frontend/webpack-stats.json'),
    }
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
MEDIA_URL = '/dmedia/'
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

VUE_ROOT = os.path.join(BASE_DIR, "frontend\\static\\")
