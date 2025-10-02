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

    def test_shorten_and_resolve_url(self) -> None:
        client = APIClient()
        response = client.post(
            reverse("shorten-url"),
            {"url": "http://example.com/very-very/long/url/even-longer"},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data = response.json()
        self.assertIn('short_url', data)

        short_url = data["short_url"]
        short_id = short_url.rstrip("/").split("/")[-1]

        # Resolve the short URL
        response = self.client.get(reverse("redirect", args=[short_id]))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response["Location"], "http://example.com/very-very/long/url/even-longer")
