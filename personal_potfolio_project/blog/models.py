from django.db import models
from datetime import date

class MyBlog(models.Model):
    #Different type of fields listed there : https://docs.djangoproject.com/fr/3.1/ref/models/fields/#django.db.models.CharField
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=1500)
    content = models.TextField()
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.title