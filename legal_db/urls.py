from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("case/", views.case_detail),   # Temporary route just to show the layout
    path("cases/", views.case_index),
]
