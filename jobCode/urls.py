"""
URL configuration for jobCode project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from jobCode.views.version import VersionView
from jobCode.views.location import LocationView
from jobCode.views.logger import LoggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('version/', VersionView.as_view(), name='version'),
    path('location/', LocationView.as_view(), name='location'),
    path('logs/', LoggerView.as_view(), name='logs-list'),
]
