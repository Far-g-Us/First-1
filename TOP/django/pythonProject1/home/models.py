from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)                      # Строка с огранич знаками
    desc = models.CharField(max_length=150)                      # Строка с огранич знаками
    image = models.ImageField(upload_to='block/image/')          # Строка под изображение
    date = models.DateField()                                    # Data
    url = models.URLField()                                      # Ссылка