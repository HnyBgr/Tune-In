from django.urls import path
from . import views
from django.contrib import admin

app_name = 'main_app'

urlpatterns = [
    path('', views.index, name='index'),
    # path('login/', views.login_page, name='login_page'),
    # path('register/', views.register_page, name='register_page'),
    # path('', views.detail, name='detail'),
]