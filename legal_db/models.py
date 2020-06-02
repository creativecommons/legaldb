from django.db import models


class License(models.Model):
    code = models.CharField(max_length=12)
    title = models.CharField(max_length=50)
    version = models.CharField(max_length=25, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.code
