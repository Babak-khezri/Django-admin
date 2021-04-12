from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import format_html


# Create your models here.
class User(AbstractUser):
    STATUS_CHOICES = (
        ('m', 'male'),
        ('p', 'female')
    )
    email = models.EmailField( unique=True, max_length=254)
    name = models.CharField(max_length=70)
    image = models.ImageField(upload_to='images/profile',default='images/profile/default.jpg', blank=True)
    bio = models.TextField(blank=True)
    following = models.ManyToManyField('User', blank=True,related_name='followers')
    requests = models.ManyToManyField('User', blank=True,related_name='requested')
    website = models.URLField(blank=True)
    birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1,choices=STATUS_CHOICES,blank=True)
    is_private = models.BooleanField(default=False)
    dark_mode = models.BooleanField(default=False)
    first_name = None
    last_name = None

    REQUIRED_FIELDS = ['email','name']

    def image_tag(self):  # show image in admin panel
        return format_html(f"<img width=100 height=75 style='border-radius: 90px;width:77px;'src={self.image.url}>")
    
    def posts_to_int(self):
        return self.posts.filter(is_archived=False).count()
                