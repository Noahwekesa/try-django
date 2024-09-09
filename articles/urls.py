from django.urls import path
from . import views


app_name = "articles"

urlpatterns = [
    path("list/", views.articles_list_view, name="list"),
]
