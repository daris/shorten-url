from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status


class ShortenUrlViewTests(TestCase):
    def test_valid_input_data(self) -> None:
        client = APIClient()
        response = client.post(
            reverse("shorten-url"),
            {"url": "http://example.com/very-very/long/url/even-longer"},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data = response.json()
        self.assertIn('short_url', data)

    def test_invalid_input_data(self) -> None:
        client = APIClient()
        response = client.post(
            reverse("shorten-url"),
            {"url": "some invalid url"},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
