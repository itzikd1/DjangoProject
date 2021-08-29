from django.db import models


# Create your models here.
class Experience(models.Model):
    title = models.CharField(max_length=30)
    details = models.CharField(max_length=500, blank=True)
    startTime = models.DateTimeField()

    def __str__(self):
        return self.title
