from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("case/", views.case_detail, name="case_detail"),   # !! Temporary route just to show the layout
    path("cases/", views.case_index, name="case_index"),
    # !! Temporary routes just to show the layout
    path("scholarship/", views.case_detail, name="scholarship_detail"),
    path("scholarships/", views.temp, name="scholarship_index"),
    path("faq/", views.temp, name="faq")
]
