"""SistemaBoxeo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from Boxeo import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('boxeadores/', views.listadoBoxeadores),
    path('agregarBoxeador/', views.agregarBoxeador),
    path('eliminarBoxeador/<int:id>', views.eliminarBoxeador),
    path('actualizarBoxeador/<int:id>', views.actualizarBoxeador),
    path('torneos/', views.listadoTorneos),
    path('agregarTorneo/', views.agregarTorneo),
    path('eliminarTorneo/<int:id>',views.eliminarTorneo),
    path('actualizarTorneo/<int:id>', views.actualizarTorneo),
    path('teams/', views.listadoTeams),
    path('agregarTeam/', views.agregarTeam),
    path('eliminarTeam/<int:id>',views.eliminarTeam),
    path('actualizarTeam/<int:id>', views.actualizarTeam),
]
