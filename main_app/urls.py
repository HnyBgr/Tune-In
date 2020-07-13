from django.urls import path
from . import views
from django.contrib import admin

app_name = 'main_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('sign_up/', views.sign_up, name='sign_up'),
    # test page for animation
    path('motion/', views.motion, name='motion'),
]