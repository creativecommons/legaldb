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
    """Abstract Class to contain the commons attributes of Cases and Scholarship"""

    license = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="The Creative Commons licence associated to the legal resource.",
    )
    contributor_name = models.CharField(max_length=120)
    contributor_email = models.EmailField()
    summary = models.TextField(blank=True, null=True)
    tags = TaggableManager(blank=True)

    class Status(models.IntegerChoices):
        UNREVIEWED = 1, _("Unreviewed")
        REVIEW_IN_PROGRESS = 2, _("Review in Progress")
        PUBLISHED = 3, _("Published")
        REJECTED = 4, _("Rejected")

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

    def __str__(self):
        return self.url


class Case(LegalResource):
    name = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="If there are multiple lawsuits between the parties, please just "
        "include one here and note the others in the related cases field.",
    )
    related_cases = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="If there are multiple lawsuits between the parties in this dispute, "
        "please note additional cases here.",
    )
    country = CountryField(blank=True, null=True)
    courts = models.CharField(
        max_length=255,
        help_text="The original court name and/or English translation. If the lawsuit "
        "was filed in one court and then went to another court on appeal, please note "
        "all relevant courts here.",
    )
    background = models.TextField(
        blank=True,
        null=True,
        help_text="Describe the factual information that led to the lawsuit "
        "being filed, and explain what claims were filed in the lawsuit.",
    )
    decision_year = models.PositiveSmallIntegerField(
        blank=True, null=True, help_text="Year of case resolution."
    )
    links = models.ManyToManyField(
        Link,
        help_text="Include any links to pleadings, briefs, and opinions in the "
        "lawsuit, as well as blog posts, academic articles, or other relevant "
        "materials.",
    )

    def __str__(self):
        return self.name


class Scholarship(LegalResource):
    title = models.CharField(max_length=255, blank=True, null=True)
    publication_name = models.CharField(max_length=255, blank=True, null=True)
    publication_year = models.PositiveSmallIntegerField(blank=True, null=True)
    authors = models.CharField(max_length=255, blank=True, null=True)
    link = models.ForeignKey(
        Link, on_delete=models.CASCADE, help_text="The link to the article."
    )

    def __str__(self):
        return self.title or self.link.url


class FAQ(BaseModel, OrderedModel):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    class Meta(OrderedModel.Meta):
        ordering = ("order",)

    def __str__(self):
        return self.question
