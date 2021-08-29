from django.db import models


class Projects(models.Model):
    title = models.CharField(max_length=30)
    details = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
