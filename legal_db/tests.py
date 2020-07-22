from django.test import TestCase
from django.urls import reverse

from .factories import ScholarshipFactory
from .models import Scholarship


class ScholarshipListViewTests(TestCase):
    def test_no_scholarship(self):
        """
        When no scholarship exists, announce and verify that the page still loads.
        """
        response = self.client.get(reverse("scholarship_index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No scholarships are available.")

    def test_show_only_published(self):
        """
        Scholarship list is displayed correctly, only with articles marked with the
        status 'PUBLISHED'.
        """
        scholarships = ScholarshipFactory.create_batch(3)
        scholarships[1].status = Scholarship.Status.PUBLISHED

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
        scholarship = ScholarshipFactory()
        url = reverse("scholarship_detail", kwargs={"pk": scholarship.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

        scholarship.status = Scholarship.Status.PUBLISHED
        scholarship.save()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
