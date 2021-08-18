from django.contrib import admin
from django.urls import path
from django.templatetags.static import static
from django.views.static import serve
from django.conf.urls import url

from datasetmanager import views
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index_page, name='index'),
    path('home/', views.index_page, name='index'),
    path('', views.index_page, name='index'),
    path('upload/', views.upload_page, name='upload'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('upload_success', views.upload_success, name='upload_success'),
    path('download/', views.download_page, name='download'),
    url(r'^datasets/(?P<path>.*)$', serve, {
        'document_root' : settings.MEDIA_ROOT
    })
]
