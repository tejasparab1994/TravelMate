from django.conf.urls import url
from . import views

app_name = 'rate'

urlpatterns = [
    #/rate/
    url(r'^$', views.index, name = 'index'),

]
