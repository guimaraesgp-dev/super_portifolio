from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=50)
    github = models.URLField(max_length=300)
    linkedin = models.URLField(max_length=300)
    bio = models.TextField()

    def __str__(self):
        return self.name
