# Generated by Django 2.2.10 on 2020-02-07 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200207_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='special',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
