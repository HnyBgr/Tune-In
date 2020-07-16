from django.urls import path
from . import views
from django.contrib import admin

app_name = 'main_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('login_user/', views.login_user, name='login_user'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('logout/', views.logout_user, name='logout_user'),
    # test page for animation
    path('motion/', views.motion, name='motion'),
]