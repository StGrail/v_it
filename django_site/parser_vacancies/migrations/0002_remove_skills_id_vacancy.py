# Generated by Django 3.1.4 on 2021-01-15 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parser_vacancies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skills',
            name='id_vacancy',
        ),
    ]
