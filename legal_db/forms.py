from django.forms import BooleanField, ModelForm, modelformset_factory

from .models import Case, Link, Scholarship


class LinkForm(ModelForm):
    class Meta:
        model = Link
        exclude = ["notes"]


LinkFormset = modelformset_factory(Link, form=LinkForm, extra=3)


class CaseForm(ModelForm):
    agreement = BooleanField()

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


class ScholarshipForm(ModelForm):
    agreement = BooleanField()

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
