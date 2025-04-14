"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from main.views import *

urlpatterns = [

    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('aktyorlar/', AktyorlarAPIView.as_view()),
    path('tariflar/', TarifAPIView.as_view()),
    path('kinolar/', KinoAPIView.as_view()),
    path('aktyorlar/<int:pk>/', AktyorRetrieveUpdateDeleteAPIView.as_view()),
    path('tariflar/<int:pk>/', TarifRetrieveUpdateDeleteAPIView.as_view()),
)

urlpatterns += [
    path('i18n/', include('django.conf.urls.i18n')),  # to support language switch
]
