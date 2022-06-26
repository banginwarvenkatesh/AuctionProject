from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('reg/',views.RegistrationView.as_view(), name='reg_url'),
    path('log/', views.LoginView.as_view(), name='login_url'),
    path('out/', views.LogoutView.as_view(),name='logout'),
    path('otp', views.OTPView.as_view(), name='otp_url'),
    path('activate/<uidb64>/<token>/',views.ActivateAccountView.as_view(), name='activate'),
    path('password-reset/', views.ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='User_App/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='User_App/password_reset_complete.html'),
         name='password_reset_complete'),

    path('', views.HomeView.as_view(), name='home'),
    ]