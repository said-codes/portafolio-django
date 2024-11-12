# portfolio/models.py
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)

    def __str__(self):
        return self.title
