"""miproyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from aparcamientos import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^/?$', views.pagPrincipal, name='Muestra la pág principal'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^css/style.css$', views.css, name='Sirve el css'),
    url(r'^login/?$', views.loginUsuario, name="Login de usuarios"),
    url(r'^logout/?$', views.logoutUsuario, name="Logout de usuarios"),
    url(r'^aparcamientos/?$', views.aparcamientos,
        name='Muestra la pág con todos los aparcamientos'),
    url(r'^aparcamientos/(.*)/?$', views.pagAparcamiento,
        name='Muestra la pág del aparcamiento en cuestión'),
    url(r'^(.*)/xml/?$', views.xml, name='Canal XML'),
    url(r'^about/?$', views.about, name='Muestra la pág about'),
    url(r'^videos/?$', views.videos, name='Muestra la pág con los videos'),
    url(r'^mapa/?$', views.mapa, name='Muestra la pág con el mapa'),
    url(r'^rss/?$', views.rss, name='Canal RSS para los comentarios'),
    url(r'(.*)', views.pagUsuario, name='Muestra la pág personal del usuario'),
]
