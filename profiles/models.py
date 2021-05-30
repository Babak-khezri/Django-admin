from django.db import models
from account.models import User
from django.urls import reverse


# Create your models here.

class Profile(models.Model):
    STATUS_CHOICES = (
        ('m', 'male'),
        ('f', 'female'),
    )
    user       = models.OneToOneField(User, on_delete=models.CASCADE)
    name       = models.CharField(max_length=70)
    image      = models.ImageField(upload_to='images/profile', default='images/profile/default.jpg', blank=True)
    bio        = models.TextField(blank=True)
    website    = models.URLField(blank=True)
    birth      = models.DateField(blank=True, null=True)
    gender     = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=True)
    is_private = models.BooleanField(default=False)
    dark_mode  = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} profile'


    def get_absolute_url(self):
        return reverse('')
