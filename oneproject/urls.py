"""
URL configuration for oneproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
# from api.views import ProductViewSet

# router = DefaultRouter()
# router.register(r'products',ProductViewSet )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("app.urls")),
    path('users/',include('users.urls')),
    path('api/', include('api.urls')),
    path('api/token/', obtain_auth_token, name='api_token_auth'),

    path('api/token/',TokenObtainPairView.as_view(), name='token_objain_view'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
