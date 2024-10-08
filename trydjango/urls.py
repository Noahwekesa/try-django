from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("accounts/", include("accounts.urls")),
    path("articles/", include("articles.urls")),
    path("admin/", admin.site.urls),
]
