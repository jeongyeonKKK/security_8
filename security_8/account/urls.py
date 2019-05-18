from django.conf.urls import url
from . import views


# urlpatterns = [
#     # post views
#     url(r'^login/$', views.user_login, name='login'),
#     url(r'^logout/$', views.user_logout, name='logout'),
# ]

from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='account'),
    url(r'^login/$', auth_views.logout, {'next_page' : '/'}),
    url(r'^logout/$', auth_views.login, {'template_name' : 'account/login.html'}),
]