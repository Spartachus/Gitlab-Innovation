"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView  # new

from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('userlogged/', views.loggedin, name="userlogged"),
    path('login/', views.login, name="login"),
    path('gettingstarted/', views.gettingstarted, name="gettingstarted"),
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("user.urls")),  # new
]

if settings.DEBUG:
    # do not do this in prod
    from django.conf.urls.static import static
    # Try Django
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)