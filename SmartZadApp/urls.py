"""SmartZadApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Dashboard import views
from Users import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings  # new
from django.conf.urls.static import static  # new


app_name = 'partners'

urlpatterns = [
    path("", views.index, name='index'),
    path('admin/', admin.site.urls),
    path("accounts/", include('Users.urls')),
    path("partners/", include('partners.urls')),
    path("logout/", views.user_logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_URL)
