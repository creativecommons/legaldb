# Standard library
from http import HTTPStatus

# Third-party
from django.test import TestCase
from django.urls import reverse

from .factories import CaseFactory, ScholarshipFactory
from .models import LegalResource


class CaseListViewTests(TestCase):
    url = reverse("case_index")

    def test_no_cases(self):
        """
        Where there is no case, announce it and verify that the page still
        loads.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No cases are available.")

    def test_show_only_published(self):
        """
        Case list is displayed correctly, only with cases marked with status
        'PUBLISHED'.
        """
        CaseFactory.create_batch(3)  # Default status is 'UNREVIEWED'
        CaseFactory.create_batch(2, status=LegalResource.Status.PUBLISHED)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["cases"]), 2)
        for row in response.context["cases"]:
            self.assertEqual(row.status, LegalResource.Status.PUBLISHED)


class CaseDetailViewTests(TestCase):
    def test_show_only_published(self):
        """
        Only show details of cases with status 'PUBLISHED'. First request ask
        for a not published case, it can not be exposed. Second request is for
        a published case, therefore is okay to display the case's
        information.
        """
        case = CaseFactory()
        url = reverse("case_detail", kwargs={"pk": case.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

        case.status = LegalResource.Status.PUBLISHED
        case.save()
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)


class CaseSubmitViewTests(TestCase):
    url = reverse("case_submit")

    def test_get(self):
        """
        Check if the view of the form is returned correctly.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Case Submission")

    def test_post_success(self):
        """
        Test a submission request with the minimum data required to create a
        case.
        """
        response = self.client.post(
            self.url,
            data={
                "contributor_name": "Grace Hopper",
                "contributor_email": "grace@test.com",
                "agreement": 1,
                "country": "VE",
                "form-TOTAL_FORMS": 1,
                "form-INITIAL_FORMS": 0,
                "form-MIN_NUM_FORMS": 1,
                "form-MAX_NUM_FORMS": 1000,
                "form-0-url": "www.test.com",
            },
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(response["Location"], "/submission-result/")

    def test_post_error(self):
        """
        When data send in request is bad (not valid or incomplete) then it
        should return back to the form view and show the error(s).
        """
        response = self.client.post(
            self.url,
            data={
                # Missing contributor name and email and user agreement
                "name": "Incomplete case form",
                "form-TOTAL_FORMS": 1,
                "form-INITIAL_FORMS": 0,
                "form-MIN_NUM_FORMS": 1,
                "form-MAX_NUM_FORMS": 1000,
            },
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "This field is required")


class ScholarshipListViewTests(TestCase):
    url = reverse("scholarship_index")

    def test_no_scholarships(self):
        """
        When no scholarship exists, announce it and verify that the page still
        loads.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "No scholarships are available.")

    def test_show_only_published(self):
        """
        Scholarship list is displayed correctly, only with articles marked with
        status 'PUBLISHED'.
        """
        ScholarshipFactory.create_batch(3)  # Default status is 'UNREVIEWED'
        ScholarshipFactory.create_batch(
            2, status=LegalResource.Status.PUBLISHED
        )

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.context["scholarships"]), 2)
        for row in response.context["scholarships"]:
            self.assertEqual(row.status, LegalResource.Status.PUBLISHED)


class ScholarshipDetailViewTests(TestCase):
    def test_show_only_published(self):
        """
        Scholarship details is displayed correctly and only when is marked with
        the status 'PUBLISHED'. First request ask for a not published article,
        so details are not shown. Second request is for a published article,
        therefore is okay to display the article's information.
        """
        scholarship = ScholarshipFactory()
        url = reverse("scholarship_detail", kwargs={"pk": scholarship.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

        scholarship.status = LegalResource.Status.PUBLISHED
        scholarship.save()
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)


class ScholarshipSubmitViewTests(TestCase):
    url = reverse("scholarship_submit")

    def test_get(self):
        """
        Check if the view of the form is returned correctly.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Scholarship Submission")

    def test_post_success(self):
        """
        Test a submission request with the minimum data required to create a
        scholarship.
        """
        response = self.client.post(
            self.url,
            data={
                "contributor_name": "Grace Hopper",
                "contributor_email": "grace@test.com",
                "agreement": 1,
                "url": "www.test.com",
            },
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(response["location"], "/submission-result/")

    def test_post_error(self):
        """
        When data send in request is bad (not valid or incomplete) then it
        should return back to the form view and show the error(s).
        """
        response = self.client.post(
            self.url,
            data={
                # Missing contributor name and email, user agreement and link
                "title": "Incomplete scholarship form",
            },
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "This field is required")


class FaqViewTests(TestCase):
    def test_page_up(self):
        response = self.client.get(reverse("faq"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
