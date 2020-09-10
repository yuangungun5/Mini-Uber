# Generated by Django 2.2.10 on 2020-02-06 22:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity_level', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('LUX', 'Luxuary')], max_length=3)),
                ('arrival_after', models.DateTimeField(default=django.utils.timezone.now)),
                ('arrival_before', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('date_arrival', models.DateTimeField(default=django.utils.timezone.now)),
                ('passenger_num', models.IntegerField(default=1)),
                ('capacity_level', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('LUX', 'Luxuary')], default='S', max_length=3)),
                ('is_shared', models.BooleanField(default=False)),
                ('order_status', models.CharField(choices=[('OP', 'OPEN'), ('PD', 'PENDING'), ('ON', 'ONGOING'), ('CP', 'COMPLETED'), ('CL', 'CLOSED')], default='OP', max_length=2)),
                ('note', models.TextField(blank=True, default='', null=True)),
                ('share_flag', models.BooleanField(default=False)),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='driver', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('sharer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sharer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SharerSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=100)),
                ('passenger_num', models.IntegerField(default=1)),
                ('arrival_after', models.DateTimeField(default=django.utils.timezone.now)),
                ('arrival_before', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ShareOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passenger_num', models.IntegerField(default=1)),
                ('ride', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ride.Ride')),
                ('sharer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
