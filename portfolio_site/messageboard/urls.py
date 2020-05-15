from django.urls import path, include
from . import views

app_name='messageboard'

urlpatterns = [
    path('', views.home, name='home')
]