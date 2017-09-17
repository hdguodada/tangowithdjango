from django.conf.urls import url
from .views import hello, about


urlpatterns = [
    url(r'hello/$', hello, name='hello'),
    url(r'about/$', about, name='about'),
]
