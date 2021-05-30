from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=254)
    following = models.ManyToManyField('User', blank=True, related_name='followers')
    requests = models.ManyToManyField('User', blank=True, related_name='requested')
    first_name = None
    last_name = None

    REQUIRED_FIELDS = ['email']

    def posts_to_int(self):
        return self.posts.filter(is_archived=False).count()
