# Generated by Django 3.1.4 on 2021-02-06 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0003_trainingsamplesforrecommendation'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TrainingSamplesForRecommendation',
        ),
    ]
