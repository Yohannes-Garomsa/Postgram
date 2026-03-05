
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from core import routers

urlpatterns = [
    path('admin/', admin.site.urls),
    # CoreRoot/urls.py
    path('api/', include(routers.urlspatterns), name='api'),

]
