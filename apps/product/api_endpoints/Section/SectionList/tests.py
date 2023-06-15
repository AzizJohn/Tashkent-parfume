from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.product.models import Section


class SectionListAPITestCase(APITestCase):
    def setUp(self):
        self.section1 = Section.objects.create(name="Section 1")

        self.url = reverse("product:SectionList")

    def test_get_section_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


