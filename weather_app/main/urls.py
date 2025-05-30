from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('settings/', views.user_cities_view, name='settings'),
]
