from django.urls import path
from . import views


urlpatterns = [
    path('weather/<str:city>/', views.fetch_weather, name='fetch_weather'),
]