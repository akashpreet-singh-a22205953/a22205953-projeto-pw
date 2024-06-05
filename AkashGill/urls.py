"""AkashGill URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# urls.py

from django.contrib import admin
from django.urls import path, include   # incluir include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('noobsite/', include('noobsite.urls')),
    path('pwsite/',include('pwsite.urls')),
    path('novoapp/', include('novoapp.urls')),
    path('band/', include('Band.urls')),
    path('artigos/',include('artigos.urls')),
    path('curso/', include('curso.urls')),
    path('festivais/', include('festivais.urls')),
    path('books/', include('books.urls')),
    path('autenticar/', include('autenticar.urls')),
    path('',include('portfolio1.urls')),
    path('meteo/',include('meteo.urls')),






]
