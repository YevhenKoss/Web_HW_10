from django.contrib.auth.views import LoginView, LogoutView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import path

from . import views
from .forms import LoginForm
from .views import RegisterView, ResetPasswordView

app_name = "app_users"

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='register'),
    path('signin/', LoginView.as_view(template_name='app_users/signin.html', authentication_form=LoginForm,
                                      redirect_authenticated_user=True), name='signin'),
    path('logout/', LogoutView.as_view(template_name='app_users/logout.html', ), name='logout'),
    path('reset-password/', ResetPasswordView.as_view(), name='password_reset'),
    path('reset-password/done/', PasswordResetDoneView.as_view(template_name='app_users/password_reset_done.html'),
         name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='app_users/password_reset_confirm.html',
                                          success_url='/users/reset-password/complete/'),
         name='password_reset_confirm'),
    path('reset-password/complete/',
         PasswordResetCompleteView.as_view(template_name='app_users/password_reset_complete.html'),
         name='password_reset_complete'),
]
