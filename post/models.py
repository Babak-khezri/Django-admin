from django.db import models
from account.models import User
from django.utils.html import format_html
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    image_1 = models.ImageField(upload_to='images/1posts')
    image_2 = models.ImageField(upload_to='images/1posts',blank=True)
    image_3 =  models.ImageField(upload_to='images/1posts',blank=True)
    text = models.TextField(default=" ")
    likes = models.ManyToManyField('account.User', blank=True, related_name='liked')
    date = models.DateTimeField(auto_now_add=True)
    saves = models.ManyToManyField(User, blank=True,related_name='saved')
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.text[0:10]
    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'

    def image_tag(self):  # show image in admin panel
        return format_html(f"<img width=100 height=75 src={self.image_1.url}>")

    def get_absolute_url(self):
        return reverse('post:post_detail', args=[self.pk])
    
    def images_count(self):
        if self.image_3:
            return "012"
        if self.image_2:
            return "01"
        if self.image_1:
            return "0"
    