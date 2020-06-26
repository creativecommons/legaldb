from django.urls import path

from .views import (
    case_index,
    case_detail,
    faq,
    index,
    ScholarshipListView,
    ScholarshipDetailView,
)

urlpatterns = [
    path("", index, name="home"),
    path("cases/", case_index, name="case_index"),
    path("cases/<int:case_id>", case_detail, name="case_detail"),
    path("scholarship/", ScholarshipListView.as_view(), name="scholarship_index"),
    path(
        "scholarship/<int:pk>",
        ScholarshipDetailView.as_view(),
        name="scholarship_detail",
    ),
    path("faq/", faq, name="faq"),
]
