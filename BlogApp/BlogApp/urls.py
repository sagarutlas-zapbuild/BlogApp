"""BlogApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import urls
from django.contrib.auth import views as auth_views

from rest_framework_jwt.views import ObtainJSONWebToken, RefreshJSONWebToken

obtain_jwt_token = ObtainJSONWebToken(user_model='API.User').as_view()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('API.urls')),
    path('auth/', obtain_jwt_token),
    path('change-password/', auth_views.PasswordChangeView.as_view()),
    path('reset-password/', auth_views.PasswordResetView.as_view()),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset-password/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-passwordreset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
