from django.urls import path

from . import views

urlpatterns = [
    path('', views.broadcast, name='broadcast'),
    path('about/', views.about, name='about')
]