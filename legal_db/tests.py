from django.test import TestCase
from django.urls import reverse

from .models import Link, Scholarship


def create_scholarship():
    """
    Create a dummy scholarship and link for tests.
    """
    link = Link.objects.create(url="example.com")
    scholarship = Scholarship.objects.create(
        contributor_name="Testing Contributor",
        contributor_email="test@test.co",
        title="A Test Title",
        publication_year=2010,
        link_id=link.id,
    )
    return scholarship


def fill_db_with_some_scholarship():
    create_scholarship()  # Default status is "UNREVIEWED"
    scholarship = create_scholarship()
    scholarship.status = Scholarship.Status.REVIEW_IN_PROGRESS
    scholarship.save()
    scholarship = create_scholarship()
    scholarship.status = Scholarship.Status.PUBLISHED
    scholarship.save()


class ScholarshipListViewTests(TestCase):
    def test_no_scholarship(self):
        """
        When no scholarship exists, announce and verify that the page still loads.
        """
        response = self.client.get(reverse("scholarship_index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No scholarship article are available.")

    def test_show_only_published(self):
        """
        Scholarship list is displayed correctly, only with articles marked with the
        status 'PUBLISHED'.
        """
        fill_db_with_some_scholarship()
        response = self.client.get(reverse("scholarship_index"))
        self.assertEqual(response.status_code, 200)
        for row in response.context["scholarships"]:
            self.assertEqual(row.status, Scholarship.Status.PUBLISHED)


class ScholarshipDetailViewTests(TestCase):
    def test_show_only_published(self):
        """
        Scholarship details is displayed correctly and only when is marked with the
        status 'PUBLISHED'. First request ask for a not published article, so details
        are not shown. Second request is for an published article, therefore is okay
        to display the article's information.
        """
        scholarship = create_scholarship()
        url = reverse("scholarship_detail", kwargs={"pk": scholarship.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

        scholarship.status = Scholarship.Status.PUBLISHED
        scholarship.save()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
