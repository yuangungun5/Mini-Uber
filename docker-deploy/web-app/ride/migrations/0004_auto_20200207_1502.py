# Generated by Django 2.2.10 on 2020-02-07 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0003_auto_20200207_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='capacity_level',
            field=models.CharField(blank=True, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('LUX', 'Luxuary')], max_length=3, null=True),
        ),
    ]
