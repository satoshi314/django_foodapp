"""
WSGI config for MyFood project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
#from whitenoise.django import DjangoWhiteNoise
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyFood.settings')

<<<<<<< HEAD

application = Cling(get_wsgi_application())
=======
 
# application = Cling(get_wsgi_application())
>>>>>>> 0c6c5f4004c9f8afcfcda65153a9f7e9996a9769

#whitenoise用の古い設定 最新版ではこのファイルでの設定不要？
application = get_wsgi_application()
application = DjangoWhiteNoise(application)