from django.db import models


class Repository(models.Model):
    """Model representing dataset repository"""

    name = models.CharField(max_length=255)
    id = models.CharField(max_length=255, primary_key=True)
    doi = models.CharField(max_length=255, unique=True)
    api_url = models.URLField()
    last_update = models.DateField()

    def __str__(self):
        return self.name
