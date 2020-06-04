from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from ordered_model.models import OrderedModel


class BaseModel(models.Model):
    notes = models.TextField(
        blank=True, null=True, help_text="Internal notes or description."
    )
    created_at = models.DateTimeField(
        auto_now_add=True, help_text="A timestamp of when the object is first created."
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="A timestamp of the last time when the object was modified.",
    )

    class Meta:
        abstract = True


class LegalResource(BaseModel):
    license = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="The Creative Commons licence associated to the case.",
    )
    contributor_name = models.CharField(max_length=120)
    contributor_email = models.EmailField()
    contribution_credit_requested = models.BooleanField(
        help_text="Whether or not show credit to contributor by name on the site."
    )
    link = models.URLField(
        max_length=2000,
        help_text="Link to the Original Version of Decision (for Case) or the Article (for Scholarship).",
    )
    country = CountryField()
    summary = models.TextField(blank=True, null=True)

    class Status(models.IntegerChoices):
        UNREVIEWED = 1, _("Unreviewed")
        REVIEW = 2, _("Review")
        IN_PROGRESS = 3, _("In progress")
        PUBLISHED = 4, _("Published")
        REJECTED = 5, _("Rejected")

    status = models.PositiveSmallIntegerField(
        choices=Status.choices,
        default=Status.UNREVIEWED,
        help_text="The stage of the review process where the resource is.",
    )

    class Meta:
        abstract = True


class Case(LegalResource):
    name = models.CharField(max_length=200, blank=True, null=True)
    case_no = models.CharField(
        max_length=50, blank=True, null=True, help_text="The number of the case."
    )
    jurisdiction = models.CharField(
        max_length=255, blank=True, null=True, help_text="Jurisdiction Within country."
    )
    court_name = models.CharField(
        max_length=255, help_text="The original court name and/or English translation."
    )
    decision_locality = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="The District/City/Circuit of decision.",
    )
    language = models.CharField(max_length=50, blank=True, null=True)
    decided_at = models.DateField(
        blank=True, null=True, help_text="The decision date of the case."
    )
    en_translation_link = models.URLField(
        max_length=2000,
        blank=True,
        null=True,
        help_text="Link to the English translation.",
    )
    cc_involvement = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Creative Commons involvement, if any.",
    )

    # TODO: Add help_text for these fields
    cc_implication = models.TextField(blank=True, null=True)
    work_type = models.CharField(max_length=100, blank=True, null=True)

    # TODO: Check if it these fields are actually used
    issue = models.CharField(max_length=200, blank=True, null=True)
    blurb = models.TextField(blank=True, null=True)
    original_blurb = models.TextField(blank=True, null=True)

    background = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Scholarship(LegalResource):
    title = models.CharField(max_length=255, blank=True, null=True)
    authors = models.CharField(max_length=255, blank=True, null=True)
    published_at = models.DateField(blank=True, null=True)
    elements_discussing = models.CharField(max_length=255, blank=True, null=True)
    journal_or_publisher = models.CharField(max_length=255, blank=True, null=True)
    categories = ArrayField(
        models.CharField(max_length=100),
        blank=True,
        null=True,
        help_text="Categories or keywords associated with the scholarship.",
    )

    def __str__(self):
        return self.title


class FAQ(BaseModel, OrderedModel):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    class Meta(OrderedModel.Meta):
        ordering = ("order",)

    def __str__(self):
        return self.question
