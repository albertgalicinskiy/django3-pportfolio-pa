from django.db import models

# Create your models here.
# Модель для Блога

class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
