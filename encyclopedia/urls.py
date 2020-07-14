from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.entry, name="entry"),
    path("not_found/", views.not_found, name="not_found"),
    path("search/<str:title>", views.search, name="search"),
]
