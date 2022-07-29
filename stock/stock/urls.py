"""stock URL Configuration

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
from django.contrib import admin
from django.urls import path
from yuasa import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name="main"),
    path('sauron/', views.palettesSauron, name="sauron"),
    path('sauron/new/', views.sauron_new, name='sauron-new'),
    path('sauron/<int:id>/', views.sauron_detail, name="sauron-detail"),
    path('sauron/<int:id>/delete', views.sauron_delete, name="sauron-delete"),
    path('sauron/<int:id>/change', views.sauron_change, name="sauron-change"),
    path('picard/', views.palettesPicard, name="picard"),
    path('picard/new/', views.picard_new, name='picard-new'),
    path('picard/<int:id>/', views.picard_detail, name="picard-detail"),
    path('picard/<int:id>/delete', views.picard_delete, name="picard-delete"),
    path('picard/<int:id>/change', views.picard_change, name="picard-change"),
]
