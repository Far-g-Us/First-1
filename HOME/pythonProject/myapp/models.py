from django.db import models

class Anketa(models.Model):
    foto = models.ImageField('Фото', upload_to='myapp/image/')
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    date_of_birth = models.DateField('Дата рождения')
    skill_1 = models.CharField('1-е умение', max_length=100)
    skill_2 = models.CharField('2-е умение', max_length=100)
    skill_3 = models.CharField('3-е умение', max_length=100)
    skill_4 = models.CharField('4-е умение', max_length=100)
    skill_5 = models.CharField('5-е умение', max_length=100)
    about_me = models.TextField('Обо мне')

    def __str__(self):
        return f"{self.foto} | {self.first_name} | {self.last_name} | {self.date_of_birth} | {self.skill_1} | {self.skill_2} | {self.skill_3} | {self.skill_4} | {self.skill_5} | {self.about_me})"