"""quiz1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from custom_auth import views
from main import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register/', views.AuthViewSet.as_view({'post': 'create'}), name='register_view'),
    path('auth/login2/', views.AuthViewSet.as_view({'post': 'retrieve'}), name='login_view'),
    path('books/', main_views.BookViewSets.as_view({'post': 'list'}), name='books')
]
