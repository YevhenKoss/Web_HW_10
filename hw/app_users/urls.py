from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .forms import LoginForm
from .views import RegisterView

app_name = "app_users"

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='register'),
    path('signin/', LoginView.as_view(
        template_name='app_users/signin.html',
        authentication_form=LoginForm,
        redirect_authenticated_user=True
    ), name='signin'),
    path('logout/', LogoutView.as_view(
            template_name='app_users/logout.html',
        ), name='logout'),
]