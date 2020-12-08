from django.db import models

# Create your models here.
class SearchQuery(models.Model):
    querystring = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    results_found = models.IntegerField(default=0)
