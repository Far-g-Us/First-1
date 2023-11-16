from django.db import models

class Anketa(models.Model):
    image = models.ImageField('Фото', upload_to='image/')
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    birth_day = models.DateField('Дата рождения')
    skill_1 = models.CharField('1-е умение', max_length=100)
    skill_2 = models.CharField('2-е умение', max_length=100)
    skill_3 = models.CharField('3-е умение', max_length=100)
    skill_4 = models.CharField('4-е умение', max_length=100)
    skill_5 = models.CharField('5-е умение', max_length=100)
    about_me = models.TextField('Обо мне', max_length=250)

    def __str__(self):
        return f"{self.first_name} | {self.last_name}"