
from django.contrib import admin
from django.urls import path,include

from . import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('main.urls')),
    path('accounts/' , include('accounts.urls')),
    path('projects/', include('projects.urls')),
    path('dashboard/', include('dashboard.urls')),
]
