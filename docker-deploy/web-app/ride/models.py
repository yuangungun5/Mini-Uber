from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Ride(models.Model):
    LEVEL_CHOICES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('LUX', 'Luxury'),
    )

    STATUS_CHOICES = (
        ('OP', 'OPEN'),
        ('PD', 'PENDING'),
        ('ON', 'ONGOING'),
        ('CP', 'COMPLETED'),
        ('CL', 'CLOSED'),
    )
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    start = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date_arrival = models.DateTimeField(default=timezone.now)
    passenger_num = models.IntegerField(default=1)
    capacity_level = models.CharField(max_length=3, choices=LEVEL_CHOICES, null=True, blank=True)
    is_shared = models.BooleanField(default=False)
    order_status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='OP')
    note = models.TextField(default='', null=True, blank=True)
    driver = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='driver')
    sharer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='sharer')
    share_passenger_num = models.IntegerField(default=0)
    share_flag = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.owner.username} requests from {self.start} to {self.destination}'

    def get_absolute_url(self):
        return reverse('ride-detail', kwargs = {'pk': self.pk})

class DriverSearch(models.Model):
    arrival_after = models.DateTimeField(default=timezone.now)
    arrival_before = models.DateTimeField(default=timezone.now)
    
class SharerSearch(models.Model):
    destination = models.CharField(max_length=100)
    passenger_num = models.IntegerField(default=1)
    arrival_after = models.DateTimeField(default=timezone.now)
    arrival_before = models.DateTimeField(default=timezone.now)
    
class ShareOrder(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, null=True, blank=True)
    sharer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    passenger_num = models.IntegerField(default=1)
