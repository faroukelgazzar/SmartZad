from django.urls import path
from Dashboard import views


urlpatterns = [
    path('', views.index, name='Dashboard'),
]