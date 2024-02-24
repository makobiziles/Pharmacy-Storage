from django.urls import path
from . import views
from .views import IndexView, SignUpView
from django.contrib.auth.views import LoginView, LogoutView
app_name = "Pharmapics"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path(
    "login/",
    LoginView.as_view(
      # name of the login template
      template_name="Pharmapics/login.html",
      # user will be redirected to index page upon successful login
      next_page="Pharmapics:index",
      redirect_authenticated_user=True,
    ),
    name="login",
  ),

    path(
        "logout/",
    # user will be redirected to index page upon logout
    LogoutView.as_view(next_page="Pharmapics:index"),
    name="logout",
  ),
    path("signup/", SignUpView.as_view(), name="signup"),
]