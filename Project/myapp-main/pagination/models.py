from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=300)
    def __str__(self):
        return self.title