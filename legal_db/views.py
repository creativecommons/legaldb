from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, TemplateView

from .forms import LinkForm, ScholarshipForm
from .models import Case, FAQ, Scholarship
from taggit.models import Tag


class HomeView(TemplateView):
    template_name = "legal_db/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cases_tags"] = Tag.objects.exclude(case=None)[:12]
        context["scholarship_tags"] = Tag.objects.exclude(scholarship=None)[:12]
        return context


class CaseListView(ListView):
    template_name = "legal_db/case/index.html"
    context_object_name = "cases"
    queryset = (
        Case.objects.filter(status=Case.Status.PUBLISHED)
        .only("country", "name", "license", "decision_year")
        .order_by("country", "name")
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.exclude(case=None)
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
    queryset = Scholarship.objects.filter(status=Scholarship.Status.PUBLISHED).order_by(
        "-publication_year", "title"
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.exclude(scholarship=None)
        return context


class ScholarshipDetailView(DetailView):
    context_object_name = "scholarship"
    template_name = "legal_db/scholarship/detail.html"
    queryset = Scholarship.objects.filter(status=Scholarship.Status.PUBLISHED)

    def get_object(self):
        obj = super().get_object()
        obj.tags = obj.tags.all()
        return obj


class FAQListView(ListView):
    model = FAQ
    template_name = "legal_db/faq.html"
    context_object_name = "faqs"


def scholarship_submit_view(request):
    """Show submission form and process the request to save an Scholarship article."""
    if request.method == "POST":
        link_form = LinkForm(request.POST)
        scho_form = ScholarshipForm(request.POST)

        if link_form.is_valid() and scho_form.is_valid():
            link = link_form.save()
            scholarship = scho_form.save(commit=False)
            scholarship.link_id = link.id
            scholarship.save()

            messages.success(request, "scholarship created")
            return redirect("submission_result")
    else:
        link_form = LinkForm()
        scho_form = ScholarshipForm()

    return render(
        request,
        "legal_db/scholarship/form.html",
        {"link_form": link_form, "scho_form": scho_form},
    )


def result_view(request):
    """
    Result page to tell the resource was successfully received.
    Redirects to home if the request does not come after a form submitted.
    """
    message = get_request_message(request)
    if not message:
        return redirect("home")

    return render(request, "legal_db/result.html", {"action": message})


def get_request_message(request):
    storage = messages.get_messages(request)
    for list in storage:
        if ("scholarship" in list.message) or ("case" in list.message):
            return list.message
