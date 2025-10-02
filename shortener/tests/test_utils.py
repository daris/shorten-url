from django.test import TestCase
import string
from shortener.utils import generate_short_id, generate_unique_short_id
from shortener.models import URL


class UtilsTests(TestCase):
    def test_generate_short_id_length(self) -> None:
        short_id = generate_short_id()
        self.assertEqual(len(short_id), 6)
        self.assertIsInstance(short_id, str)

    def test_generate_short_id_characters(self) -> None:
        short_id = generate_short_id()
        valid_chars = string.ascii_letters + string.digits
        for c in short_id:
            self.assertIn(c, valid_chars)

    def test_generate_unique_short_id_creates_unique(self) -> None:
        URL.objects.create(original_url="http://example.com", short_id="abc123")
        new_short_id = generate_unique_short_id()
        self.assertNotEqual(new_short_id, "abc123")
