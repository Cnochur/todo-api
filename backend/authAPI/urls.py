from . import views
from django.urls import path

app_name = 'authAPI'

urlpatterns = [
    path('login/', views.auth_login, name='login'),
    path('logout/', views.auth_logout, name='logout'),
    path('register/', views.auth_register, name='register'),
]

