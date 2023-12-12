from django.db import models

class SitePost(models.Model):
    title = models.CharField(max_length=100000)
    description = models.CharField(max_length=100000)
 