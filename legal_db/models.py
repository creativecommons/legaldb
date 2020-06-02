from django.contrib.postgres.fields import ArrayField
from django.db import models
from django_countries.fields import CountryField


class LegalResource(models.Model):
    license = models.CharField(max_length=25, blank=True, null=True)
    license_version = models.CharField(max_length=25, blank=True, null=True)
    is_ported = models.BooleanField(blank=True, null=True)
    contributor_name = models.CharField(max_length=120)
    contributor_email = models.EmailField()
    contribution_credit = models.BooleanField()
    link = models.URLField(max_length=2000)
    country = CountryField()
    summary = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Case(LegalResource):
    name = models.CharField(max_length=200, blank=True, null=True)
    case_no = models.CharField(max_length=50, blank=True, null=True)
    jurisdiction = models.CharField(max_length=250, blank=True, null=True)
    court_name = models.CharField(max_length=250)
    decision_district_city_circuit = models.CharField(
        max_length=250, blank=True, null=True
    )
    language = models.CharField(max_length=50, blank=True, null=True)
    decided_at = models.DateField(blank=True, null=True)
    en_translation_link = models.URLField(
        max_length=2000, blank=True, null=True
    )
    cc_involvement = models.CharField(max_length=100, blank=True, null=True)
    cc_implication = models.TextField(blank=True, null=True)
    work_type = models.CharField(max_length=100, blank=True, null=True)

    # TODO: Check if it these fields are actually used
    issue = models.CharField(max_length=200, blank=True, null=True)
    blurb = models.TextField(blank=True, null=True)
    original_blurb = models.TextField(blank=True, null=True)

    background = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)

    def __str__(self):
        return "(Case) " + self.name


class Scholarship(LegalResource):
    title = models.CharField(max_length=250, blank=True, null=True)
    authors = models.CharField(max_length=250, blank=True, null=True)
    published_at = models.DateField(blank=True, null=True)
    elements_discussing = models.CharField(
        max_length=250, blank=True, null=True
    )
    journal_or_publisher = models.CharField(
        max_length=256, blank=True, null=True
    )
    categories = ArrayField(
        models.CharField(max_length=100), blank=True, null=True
    )

    def __str__(self):
        return "(Scholarship) " + self.title


class FAQ(models.Model):
    question = models.CharField(max_length=250)
    answer = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "(FAQ) " + self.question
