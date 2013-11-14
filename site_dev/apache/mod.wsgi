import os,sys
sys.path.append('C:\\xampp\\htdocs\\Teeth_Project\\site_dev')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "site_dev.settings")

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()