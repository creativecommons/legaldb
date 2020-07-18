from django import forms

from .models import Case, Link, Scholarship


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        exclude = ["notes"]


class CaseForm(forms.ModelForm):
    agreement = forms.BooleanField()

    class Meta:
        model = Case
        fields = [
            "contributor_name",
            "contributor_email",
            "license",
            "name",
            "related_cases",
            "country",
            "courts",
            "background",
            "decision_year",
            "summary",
            "is_pending",
        ]


class ScholarshipForm(forms.ModelForm):
    agreement = forms.BooleanField()

    class Meta:
        model = Scholarship
        fields = [
            "contributor_name",
            "contributor_email",
            "license",
            "title",
            "publication_name",
            "publication_year",
            "authors",
            "summary",
        ]
