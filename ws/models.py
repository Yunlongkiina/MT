from django.db import models

# Create your models here.


class News(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    date = models.DateField()
    content = models.TextField()

    def __unicode__(self):  # unicode make code is more readable
        return self.title