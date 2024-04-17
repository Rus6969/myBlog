from django.db import models

# Create your models here.

class Post(models.Model):
    title =models.CharField(max_length=100)
    excerpt = models.CharField(max_length=300)
    image_name = models.CharField(max_length=50)
    date = models.DateField()
