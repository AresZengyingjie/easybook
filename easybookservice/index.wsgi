#coding:utf-8  
import sae  
  
from easybookservice import wsgi                       
  
application = sae.create_wsgi_app(wsgi.application)