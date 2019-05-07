from django.db import models

# Create your models here.


class Sample(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title
