# Generated by Django 3.1.2 on 2020-12-19 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0004_auto_20201207_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockhistory',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
