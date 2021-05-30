from django.db import models
from django.utils.html import format_html
from account.models import User
from django.utils import timezone
# Create your models here.


class StoryManager(models.Manager):
    def active(self):
        return self.filter(status='a')


class Story(models.Model):
    STATUS_CHOICES = (
        ('a', 'active'), ('d', 'deactive')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stories')
    image = models.ImageField(upload_to='images/story')
    date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=1, default='a', choices=STATUS_CHOICES)
    hits = models.ManyToManyField(User, blank=True)

    objects = StoryManager()

    class Meta:
        ordering = ('date',)
        verbose_name = 'استوری'
        verbose_name_plural = 'استوری ها'

    def image_tag(self):  # show image in admin panel
        return format_html(f"<img width=100 height=75 style='border-radius: 90px;width:77px;'src={self.image.url}>")

    def hits_count(self):
        return self.hits.count()


class Highlight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='highlights')
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/highlight')
    stories = models.ManyToManyField(Story,related_name='highlights')

    class Meta:
        verbose_name = 'هایلایت'
        verbose_name_plural = 'هایلایت ها'

    def __str__(self):
        return self.name

    def image_tag(self):  # show image in admin panel
        return format_html(f"<img width=100 height=75 style='border-radius: 90px;width:77px;'src={self.image.url}>")

    def stories_count(self):
        return self.stories.count()
