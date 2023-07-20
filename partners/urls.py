from django.urls import path
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from partners import views


app_name = 'partners'

urlpatterns = [
    # path('usermanager/register/', views.register, name='user_register'),
    path('createpartner/', views.new_partner, name='new_partner'),
    # path("logout/", views.user_logout, name='logout'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='/accounts/login'), name='logout'),
    # path('profile/',  login_required(UserView.as_view()), name='profile'),
    # path('register/', views.signup, name='signup'),
    # path("", views.user_login, name='index'),
]
