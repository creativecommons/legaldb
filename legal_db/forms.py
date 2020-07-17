from django import forms

from .models import Link, Scholarship


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        exclude = ["notes"]


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
