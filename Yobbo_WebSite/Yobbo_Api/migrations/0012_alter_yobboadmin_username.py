# Generated by Django 5.0.1 on 2024-01-13 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Yobbo_Api', '0011_auto_20240113_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yobboadmin',
            name='username',
            field=models.CharField(default=models.CharField(max_length=25), max_length=25),
        ),
    ]
