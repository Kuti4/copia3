from django.contrib import admin
from django.urls import path
from comments.views import showcomments
from reglog import views as reglogin
from django.contrib.auth import views as authViews

urlpatterns = [
    path('register/', reglogin.register, name='register'),
    path('login/', reglogin.user_login, name='login'),
    path('password-reset/', authViews.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', authViews.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/', authViews.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', authViews.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
