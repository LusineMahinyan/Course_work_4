from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core.views import HomeView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("clients/", include("clients.urls")),
    path("mailings/", include("mailings.urls")),
    path("users/", include("users.urls")),

    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    path("password-reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("", HomeView.as_view(), name="home"),
]
