from django.conf.urls import url
from . import views

app_name = 'myride'

urlpatterns = [
    #/myride/
    url(r'^$', views.index, name = 'index'),
    
]
