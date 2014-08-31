import os, sys  
#project=os.path.dirname(os.path.realpath(__file__))
sys.path.append("e:/website")
sys.path.append("e:/website/jasper")
os.environ['DJANGO_SETTINGS_MODULE'] = 'jasper.settings'  

import django.core.handlers.wsgi  
application = django.core.handlers.wsgi.WSGIHandler()  