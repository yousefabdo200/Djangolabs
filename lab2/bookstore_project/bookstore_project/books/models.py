from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    rate = models.FloatField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
