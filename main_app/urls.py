from django.urls import path
from . import views
from django.contrib import admin

app_name = 'main_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('motion/', views.motion, name='motion'),
    path('sign_up/', views.sign_up, name='sign_up'),
]