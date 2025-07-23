from django.db import models

# Create your models here.

class URL(models.Model):
    original_url = models.URLField()
    short_id = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f'{self.original_url} - {self.short_id}'