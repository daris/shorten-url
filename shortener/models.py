from django.db import models


class URL(models.Model):
    original_url = models.URLField()
    short_id = models.CharField(max_length=10, unique=True)

    def __str__(self) -> str:
        return f'{self.original_url} - {self.short_id}'
