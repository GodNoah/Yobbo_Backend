# Generated by Django 5.0.1 on 2024-01-12 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Yobbo_Api', '0004_remove_yobboadmin_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yobboadmin',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='yobboadmin',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]