from django.db import models

class Task(models.Model):
    title = models.CharField("Название", max_length=50)
    task = models.TextField('Описание')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

class Shablon(models.Model):
    zagol = models.CharField("Заголовок", max_length=60)
    texts = models.TextField('Основной текст')

    def __str__(self):
        return self.zagol

    class Mel:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
