from django.conf.urls import *
from blog.views import  *

 
urlpatterns = patterns('',
                      (r'archer$', online),
                      (r'app$', app),
                      (r'deploy$', deploy),
                      (r'help$', help),
                      ('Jpaas$', jpaas),
                      url(r'^$',archive),
                      )
