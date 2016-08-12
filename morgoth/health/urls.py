from django.conf.urls import url

from morgoth.health.api import views

app_name = 'health'

urlpatterns = [
    url(r'^__version__', views.version, name='version'),
    url(r'^__heartbeat__', views.heartbeat, name='heartbeat'),
    url(r'^__lbheartbeat__', views.lbheartbeat, name='lbheartbeat'),
]
