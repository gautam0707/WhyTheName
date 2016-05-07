from django.db import models


class Content(models.Model):
    searchText = models.TextField()
    whyTheName = models.TextField()
    imageId = models.TextField()