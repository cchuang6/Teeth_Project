import os,sys
#os.environ['PATH'] = 'C:\\OSGeo4W\\bin;' + os.environ['PATH']
print os.environ['PATH']
sys.path.append('C:\\xampp\\htdocs\\Teeth_Project')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "site_dev2.settings")

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()