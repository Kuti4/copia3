"""tuning URL Configuration

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
from django.urls import path

from reglog import views as reglogin
from comments import views as comment
from .views import index
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('register/', reglogin.register, name='register'),
    path('login/', authViews.LoginView.as_view(next_page='/'), name='login'),
    path('comments/', comment.showcomments, name='comments'),
    path('exit/', authViews.LogoutView.as_view(next_page='/'), name='exit'),

    path('password-reset/', authViews.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', authViews.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/', authViews.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', authViews.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]