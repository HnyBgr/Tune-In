from django.urls import path
from . import views

app_name = 'tune_in'
urlpatterns = [
    path('', views.index, name='index'),
]