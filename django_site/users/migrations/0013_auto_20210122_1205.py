# Generated by Django 3.1.4 on 2021-01-22 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20210122_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='vacancy',
        ),
        migrations.AddField(
            model_name='rating',
            name='vacancy',
            field=models.ManyToManyField(to='users.Vacancies'),
        ),
    ]
