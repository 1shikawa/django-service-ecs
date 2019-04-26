from django.db import models

# Create your models here.
class Sample(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Test(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title