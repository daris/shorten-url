import string
import random
from .models import URL


def generate_short_id(length: int = 6) -> str:
    """Generate a random short_id consisting of letters and digits."""
    characters = string.ascii_letters + string.digits  # a-zA-Z0-9
    return ''.join(random.choices(characters, k=length))


def generate_unique_short_id(length: int = 6) -> str:
    while True:
        short_id = generate_short_id(length)
        if not URL.objects.filter(short_id=short_id).exists():
            return short_id
