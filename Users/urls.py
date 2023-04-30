from django.urls import path
from Users import views

urlpatterns = [
    path('usermanager/register/', views.register, name='user_register'),
    path('login/', views.login, name='user_login'),
]
