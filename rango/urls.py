from django.conf.urls import url
from .views import IndexView, AboutView, DetailView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='hello'),
    url(r'about/$', AboutView.as_view(), name='about'),
    url(r'category/(?P<category_name_slug>[\w\-]+)/$', DetailView.as_view(), name='detail'),
]
