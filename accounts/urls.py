from django.urls import path
from . import views


urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view),
    path("signup/", views.register_view, name="signup"),
]
