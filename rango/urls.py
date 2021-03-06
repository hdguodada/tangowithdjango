from django.conf.urls import url
from .views import IndexView, AboutView, DetailView, Add_category, Add_Page, RegisterView, LoginView, LogoutView
from .views import BootStrapView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'about/$', AboutView.as_view(), name='about'),
    url(r'category/(?P<category_name_slug>[\w\-]+)/$', DetailView.as_view(), name='category'),
    url(r'add_category/$', Add_category.as_view(), name='add_category'),
    url(r'add_page/(?P<category_name_slug>[\w\-]+)/$', Add_Page.as_view(), name='add_page'),
    url(r'register/$', RegisterView.as_view(), name='register'),
    url(r'login/$', LoginView.as_view(), name='login'),
    url(r'logout/$', LogoutView.as_view(), name='logout'),
    url(r'base/$', BootStrapView.as_view(), name='base')
]
