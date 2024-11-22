from django.db import models
from tinymce.models import HTMLField


class Project(models.Model):
    title = models.CharField(max_length=100)
    content = HTMLField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title