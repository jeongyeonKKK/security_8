"""security_8 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from account import views as auth_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', auth_views.IndexView.as_view(), name='root'),
    url(r'^account/', include('django.contrib.auth.urls')),
    url(r'^account/signup/$', auth_views.CreateUSerView.as_view(), name='signup'),
    url(r'^account/signup/done/$', auth_views.RegisteredView.as_view(), name='create_user_done'),
    url(r'^chat/', include('chat.urls')),
]