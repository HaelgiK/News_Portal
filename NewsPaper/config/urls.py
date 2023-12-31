"""
URL configuration for config project.

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
from django.urls import path, include

urlpatterns = [
    # подключаем встроенные эндопинты для работы с локализацией
    path('i18n/', include('django.conf.urls.i18n')),
    # путь к панели администратора
    path('admin/', admin.site.urls),
    # перенаправление корневой страницы в приложение protect
    path('', include('protect.urls')),
    path('sign/', include('sign.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('news/', include('news.urls')),
    # перенаправление на ‘accounts/’ для всех URL,
    # которые будут управляться подключенным пакетом
    path('accounts/', include('allauth.urls')),
]
