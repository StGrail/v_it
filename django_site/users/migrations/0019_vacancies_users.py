# Generated by Django 3.1.4 on 2021-01-23 09:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20210122_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancies',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
