from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField('Заголовок', max_length=50)                         # Строка с огранич знаками
    desc = models.TextField('Описание')                                          # Строка с огранич знаками
    image = models.ImageField('Изображение', upload_to='block/image/')           # Строка под изображение
    date = models.DateField('Дата')                                              # Data
    url = models.URLField('Доп. источник', blank=False)                          # Ссылка

    def __str__(self):
        return f"{self.title} | {self.date}"