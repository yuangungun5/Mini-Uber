# Generated by Django 2.2.10 on 2020-02-07 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0002_remove_driversearch_capacity_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='capacity_level',
            field=models.CharField(blank=True, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('LUX', 'Luxuary')], default='S', max_length=3, null=True),
        ),
    ]
