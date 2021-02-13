from django.db import models

class MyProject(models.Model):
    #Different type of fields listed there : https://docs.djangoproject.com/fr/3.1/ref/models/fields/#django.db.models.CharField
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=1500)
    #content = models.TextField()
    image = models.ImageField(upload_to='portfolio/images/', max_length=100)
    url = models.URLField(blank=True)
