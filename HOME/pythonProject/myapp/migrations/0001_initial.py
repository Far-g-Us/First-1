# Generated by Django 4.2.7 on 2023-11-16 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anketa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/', verbose_name='Фото')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('birth_day', models.DateField(verbose_name='Дата рождения')),
                ('skill_1', models.CharField(max_length=100, verbose_name='1-е умение')),
                ('skill_2', models.CharField(max_length=100, verbose_name='2-е умение')),
                ('skill_3', models.CharField(max_length=100, verbose_name='3-е умение')),
                ('skill_4', models.CharField(max_length=100, verbose_name='4-е умение')),
                ('skill_5', models.CharField(max_length=100, verbose_name='5-е умение')),
                ('about_me', models.TextField(max_length=250, verbose_name='Обо мне')),
            ],
        ),
    ]
