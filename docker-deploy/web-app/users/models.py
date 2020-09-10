from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):

    LEVEL_CHOICES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('LUX', 'Luxury'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    is_driver = models.BooleanField(default=False)

    name = models.CharField(max_length=30, default='')
    licence = models.CharField(max_length=12,default='000000000000')
    car_id = models.CharField(max_length=10,default='CDC-000000')
    level = models.CharField(max_length=3, choices=LEVEL_CHOICES, default='S')
    max_passenger = models.IntegerField(default=4)
    special = models.TextField(max_length=100, blank=True, null=True)


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, **kwargs):
        super().save( **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

'''
class Driver(models.Model):
    LEVEL_CHOICES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('LUX', 'Luxuary'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default='')
    licence = models.CharField(max_length=12,default='000000000000')
    car_id = models.CharField(max_length=10,default='CDC-000000')
    level = models.CharField(max_length=3, choices=LEVEL_CHOICES, default='S')

    def save(self, **kwargs):
        super().save()
'''
