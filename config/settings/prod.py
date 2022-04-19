from .base import *
import os

#ALLOWED_HOSTS = ['172.30.1.21', 'testbbiome.tk']
ALLOWED_HOSTS = ['172.30.1.21']
STATIC_ROOT = BASE_DIR / 'static'
#STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATICFILES_DIRS = []
# concept addon