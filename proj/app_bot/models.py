from django.db import models

# Create your models here.


class User(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Chat(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    users = models.ManyToManyField(User)

    class Meta:
        verbose_name = "Чат"
        verbose_name_plural = "Чаты"
