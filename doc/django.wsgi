import os, sys  
#Calculate the path based on the location of the WSGI script.  
apache_configuration= os.path.dirname(__file__)  
project = os.path.dirname(apache_configuration)  
workspace = os.path.dirname(project)  
  
#  
os.chdir('e:/website/jasper')  
sys.stdout = sys.stderr
sys.path.append(workspace)  
  
#print workspace   
sys.path.append(workspace + "jasper")  
#sys.stdout = sys.stderr
#path = os.path.dirname(__file__)
#print path
#if path not in sys.path:
#    sys.path.append(path)
#project = os.path.join(path,"jasper")
#print project
#if project not in sys.path:
#    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'jasper.settings'  

import django.core.handlers.wsgi  
application = django.core.handlers.wsgi.WSGIHandler()  