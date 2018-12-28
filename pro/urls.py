from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index ,name="index"),
    url(r'^sign/$', views.sign ,name="sign"),
    url(r'^send_data/$', views.send_data ,name="in"),
    url(r'^log/$', views.log ,name="india"),
    url(r'^home/$', views.home ,name="homepage"),
    url(r'^home/port/$', views.port ,name="portfolio"),
    url(r'^home/docu/$', views.docu ,name="document"),
    url(r'^home/dash/$', views.dash ,name="dashboard"),
    url(r'url1/', views.url1 ,name="url"),
    url(r'links/', views.links ,name="link"),
    url(r'texts/', views.texts ,name="li"),

   
    
    

]
