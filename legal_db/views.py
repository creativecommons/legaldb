# Third-party
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, TemplateView
from taggit.models import Tag

from .forms import CaseForm, LinkForm, LinkFormset, ScholarshipForm, SearchForm
from .models import FAQ, Case, Link, Scholarship


class HomeView(TemplateView):
    template_name = "legal_db/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cases_tags"] = Tag.objects.exclude(case=None)[:12]
        context["scholarship_tags"] = Tag.objects.exclude(scholarship=None)[
            :12
        ]
        return context


class CaseListView(ListView):
    template_name = "legal_db/case/index.html"
    context_object_name = "cases"

    def get_queryset(self):
        """
        Get only rows with PUBLISHED status and filtered by user input and
        tags.
        """
        qs = Case.objects.filter(status=Case.Status.PUBLISHED).only(
            "country", "name", "license", "decision_year"
        )

        keywords = self.request.GET.get("keywords")
        if keywords:
            attributes = [
                "country",
                "name",
                "courts",
                "related_cases",
                "background",
                "summary",
                "license",
                "decision_year",
            ]
            lookups = build_filters(attributes, keywords)
            qs = qs.filter(lookups)

        tags = self.request.GET.getlist("tags[]")
        if tags:
            qs = qs.filter(tags__name__in=tags)

        return qs.order_by("country", "name")

    def get_context_data(self, **kwargs):
        """
        Append search form and tags marking the selected ones.
        """
        context = super().get_context_data(**kwargs)
        selected_tags = self.request.GET.getlist("tags[]")
        tags = []
        for tag in Tag.objects.exclude(case=None).order_by("name"):
            checked = True if tag.name in selected_tags else False
            tags.append({"name": tag, "checked": checked})
        context["tags"] = tags
        context["form"] = SearchForm(self.request.GET)
        return context


class CaseDetailView(DetailView):
    template_name = "legal_db/case/detail.html"
    context_object_name = "case"
    queryset = Case.objects.filter(status=Case.Status.PUBLISHED)

    def get_object(self):
        obj = super().get_object()
        obj.tags = obj.tags.order_by("name").all()
        obj.link_list = obj.links.all()
        return obj


class ScholarshipListView(ListView):
    template_name = "legal_db/scholarship/index.html"
    context_object_name = "scholarships"

    def get_queryset(self):
        """
        Get only rows with PUBLISHED status and filtered by user input.
        """
        qs = Scholarship.objects.filter(status=Scholarship.Status.PUBLISHED)

        keywords = self.request.GET.get("keywords")
        if keywords:
            attributes = [
                "publication_year",
                "title",
                "authors",
                "summary",
                "license",
            ]
            lookups = build_filters(attributes, keywords)
            qs = qs.filter(lookups)

        tags = self.request.GET.getlist("tags[]")
        if tags:
            qs = qs.filter(tags__name__in=tags)

        return qs.order_by("-publication_year", "title")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        selected_tags = self.request.GET.getlist("tags[]")
        tags = []
        for tag in Tag.objects.exclude(scholarship=None).order_by("name"):
            checked = True if tag.name in selected_tags else False
            tags.append({"name": tag, "checked": checked})
        context["tags"] = tags
        context["form"] = SearchForm(self.request.GET)
        return context


class ScholarshipDetailView(DetailView):
    context_object_name = "scholarship"
    template_name = "legal_db/scholarship/detail.html"
    queryset = Scholarship.objects.filter(status=Scholarship.Status.PUBLISHED)

    def get_object(self):
        obj = super().get_object()
        obj.tags = obj.tags.order_by("name").all()
        return obj


class FAQListView(ListView):
    model = FAQ
    template_name = "legal_db/faq.html"
    context_object_name = "faqs"


def case_submit_view(request):
    """Show submission form and process the request to save a legal Case."""
    if request.method == "POST":
        link_formset = LinkFormset(request.POST)
        case_form = CaseForm(request.POST)
        if link_formset.is_valid() and case_form.is_valid():
            links = link_formset.save()
            case = case_form.save()
            for link in links:
                case.links.add(link)

            messages.success(request, "case created")
            return redirect("submission_result")
    else:
        link_formset = LinkFormset(queryset=Link.objects.none())
        case_form = CaseForm()

    return render(
        request,
        "legal_db/case/form.html",
        {"link_formset": link_formset, "case_form": case_form},
    )


def scholarship_submit_view(request):
    """
    Show submission form and process the request to save an Scholarship
    article.
    """
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
    messages_list = messages.get_messages(request)
    return next(
        (
            msg.message
            for msg in messages_list
            if "scholarship" in msg.message or "case" in msg.message
        ),
        None,
    )


def build_filters(attributes, keywords):
    filters = Q()
    for attr in attributes:
        expr = f"{attr}__icontains"
        filters |= Q(**{expr: keywords})
    return filters
