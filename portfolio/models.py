from django.db import models

# Create your models here.

# Класс для создания модели БД и взаимодействия с БД

class Project(models.Model):

    # тема из портфолио на главной странице
    title = models.CharField(max_length=100)

    # описание тема из портфолио на главной странице
    descriptiion = models.CharField(max_length=250)

    # изображение темы из портфолио на главной странице
    image = models.ImageField(upload_to='portfolio/images')

    # URL для картинок ввиде ссылки при нажатии которые будут открываться в
    # новой вкладке исп-ся - blank=True
    url = models.URLField(blank=True)
