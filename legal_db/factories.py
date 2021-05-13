# Third-party
import factory
from factory.django import DjangoModelFactory

from . import models


class LinkFactory(DjangoModelFactory):
    class Meta:
        model = models.Link

    url = "https://example.com"
    title = "Example link"
    label = "testing"


class CaseFactory(DjangoModelFactory):
    class Meta:
        model = models.Case

    name = "Test Case Name"
    country = "US"
    contributor_name = "John Doe"
    contributor_email = "john@test.com"


class ScholarshipFactory(DjangoModelFactory):
    class Meta:
        model = models.Scholarship

    contributor_name = "Grace Hopper"
    contributor_email = "grace@test.com"
    title = "Test Title"
    publication_year = 2010
    link = factory.SubFactory(LinkFactory)
