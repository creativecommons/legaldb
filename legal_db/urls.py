from django.urls import path

from .views import (
    CaseListView,
    CaseDetailView,
    case_submit_view,
    FAQListView,
    HomeView,
    result_view,
    ScholarshipListView,
    ScholarshipDetailView,
    scholarship_submit_view,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("cases/", CaseListView.as_view(), name="case_index"),
    path("cases/<int:pk>/", CaseDetailView.as_view(), name="case_detail"),
    path("cases/submit/", case_submit_view, name="case_submit"),
    path("scholarship/", ScholarshipListView.as_view(), name="scholarship_index"),
    path(
        "scholarship/<int:pk>/",
        ScholarshipDetailView.as_view(),
        name="scholarship_detail",
    ),
    path("scholarship/submit/", scholarship_submit_view, name="scholarship_submit"),
    path("faq/", FAQListView.as_view(), name="faq"),
    path("submission-result/", result_view, name="submission_result"),
]
