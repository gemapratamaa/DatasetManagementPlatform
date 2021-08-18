"""datasetmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from datasetmanager import views
from . import settings
from django.templatetags.static import static
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index_page, name='index'),
    path('home/', views.index_page, name='index'),
    path('', views.index_page, name='index'),
    path('upload/', views.upload_page, name='upload'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('download/', views.download_page, name='download'),
    url(r'^datasets/(?P<path>.*)$', serve, {
        'document_root' : settings.MEDIA_ROOT
    })
]
