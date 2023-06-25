from django.urls import path
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from Users import views



app_name = 'Users'

urlpatterns = [
    #path('usermanager/register/', views.register, name='user_register'),
    path('login/', views.user_login, name='login'),
    path("logout/", views.user_logout, name='logout'),
    #path('logout/', auth_views.LogoutView.as_view(next_page='/accounts/login'), name='logout'),
    #path('profile/',  login_required(UserView.as_view()), name='profile'),
    path('registers/', views.signup, name='signup'),
    path("", views.user_login, name='index'),
]
