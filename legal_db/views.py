from legal_db.models import Case, FAQ, Scholarship
from taggit.models import Tag

from django.shortcuts import render
from django.views.generic import DetailView, ListView


def index(request):
    return render(request, "legal_db/index.html")


class CaseListView(ListView):
    template_name = "legal_db/case/index.html"
    context_object_name = "cases"
    queryset = Case.objects \
        .filter(status=Case.Status.PUBLISHED) \
        .only("country", "name", "license", "decision_year")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.exclude(scholarship=None)
        return context


class CaseDetailView(DetailView):
    template_name = "legal_db/case/detail.html"
    model = Case
    context_object_name = "case"

    def get_object(self):
        obj = super().get_object()
        obj.tags = obj.tags.all()
        obj.link_list = obj.links.all()
        return obj


class ScholarshipListView(ListView):
    template_name = "legal_db/scholarship/index.html"
    context_object_name = "scholarships"
    queryset = Scholarship.objects\
        .filter(status=Scholarship.Status.PUBLISHED)\
        .only("title", "authors", "license", "publication_year")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.exclude(scholarship=None)
        return context


class ScholarshipDetailView(DetailView):
    model = Scholarship
    context_object_name = "scholarship"
    template_name = "legal_db/scholarship/detail.html"

    def get_object(self):
        obj = super().get_object()
        obj.tags = obj.tags.all()
        return obj


class FAQListView(ListView):
    model = FAQ
    template_name = "legal_db/faq.html"
    context_object_name = 'faqs'
