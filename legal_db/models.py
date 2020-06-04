from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from ordered_model.models import OrderedModel
from taggit.managers import TaggableManager


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
        help_text="The Creative Commons licence associated to the legal resource.",
    )
    contributor_name = models.CharField(max_length=120)
    contributor_email = models.EmailField()
    country = CountryField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    tags = TaggableManager()

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


class Link(BaseModel):
    url = models.URLField(max_length=2000)
    title = models.CharField(max_length=255, blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)


class Case(LegalResource):
    name = models.CharField(max_length=200, blank=True, null=True)
    case_no = models.CharField(
        max_length=50, blank=True, null=True, help_text="The number of the case."
    )
    court_names = models.CharField(
        max_length=255,
        help_text="The original court name and/or English translation. If the lawsuit "
        "was filed in one court and then went to another court on appeal, please note all relevant courts here.",
    )
    jurisdiction = models.CharField(
        max_length=255, blank=True, null=True, help_text="Jurisdiction within country."
    )
    decision_locality = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="The district, city or circuit of decision.",
    )
    language = models.CharField(max_length=50, blank=True, null=True)
    decision_year = models.PositiveSmallIntegerField(
        blank=True, null=True, help_text="The decision year of the case."
    )
    en_translation_link = models.URLField(
        max_length=2000,
        blank=True,
        null=True,
        help_text="Link to the English translation.",
    )
    related_cases = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="If there are multiple lawsuits between the parties in this dispute,"
        " please note additional cases here.",
    )
    links = models.ManyToManyField(Link)
    cc_involvement = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Creative Commons involvement, if any.",
    )
    cc_implication = models.TextField(blank=True, null=True)
    background = models.TextField(
        blank=True,
        null=True,
        help_text="Describe the factual information that led to the lawsuit "
        "being filed, and explain what claims were filed in the lawsuit.",
    )
    result = models.TextField(
        blank=True, null=True, help_text="The resolution of the case."
    )

    def __str__(self):
        return self.name


class Scholarship(LegalResource):
    title = models.CharField(max_length=255, blank=True, null=True)
    authors = models.CharField(max_length=255, blank=True, null=True)
    publication_year = models.PositiveSmallIntegerField(blank=True, null=True)
    journal_or_publisher = models.CharField(max_length=255, blank=True, null=True)
    link = models.ForeignKey(
        Link, on_delete=models.CASCADE, help_text="The link to the article."
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
