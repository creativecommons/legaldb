from django.urls import path

from .views import (
    CaseListView,
    CaseDetailView,
    FAQListView,
    HomeView,
    ScholarshipListView,
    ScholarshipDetailView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("cases/", CaseListView.as_view(), name="case_index"),
    path("cases/<int:pk>", CaseDetailView.as_view(), name="case_detail"),
    path("scholarship/", ScholarshipListView.as_view(), name="scholarship_index"),
    path(
        "scholarship/<int:pk>",
        ScholarshipDetailView.as_view(),
        name="scholarship_detail",
    ),
    path("faq/", FAQListView.as_view(), name="faq"),
]
