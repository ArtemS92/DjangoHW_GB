from django.urls import path, include
from . import views


urlpatterns = [
    path('main/', views.main, name='main'),
    path('about_me/', views.about_me, name='about_me'),

]