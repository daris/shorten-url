from django.db import models


class URL(models.Model):
    original_url = models.URLField()
    short_id = models.CharField(max_length=10, unique=True)
