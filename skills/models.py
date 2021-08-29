from django.db import models


class Skills(models.Model):
    title = models.CharField(max_length=30)
    details = models.CharField(max_length=500, blank=True)
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

