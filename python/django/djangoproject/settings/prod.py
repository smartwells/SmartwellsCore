from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['*']	# разрешаем доступ с любого IP

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': '',
        'STATS_FILE': os.path.join(BASE_DIR, 'frontend/webpack-stats-prod.json'),
    }
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL = '/dmedia/'
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

VUE_ROOT = os.path.join(BASE_DIR, "frontend\\dist\\")
#VUE_ROOT = os.path.join(os.path.join(BASE_DIR, "frontend"), "dist")
