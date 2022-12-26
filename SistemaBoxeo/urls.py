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
from api import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('boxeador/', views.Boxeador_list.as_view()),
    path('boxeador/<int:pk>', views.Boxeador_detail.as_view()),
    path('torneo/', views.Torneo_list.as_view()),
    path('torneo/<int:pk>', views.Torneo_detail.as_view()),
    path('team/', views.Team_list.as_view()),
    path('team/<int:pk>', views.Team_detail.as_view()),
]
