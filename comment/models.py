from django.db import models
from account.models import User
from post.models import Post
# Create your models here.


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self',default=None, null=True, blank = True, on_delete=models.CASCADE, related_name='replays')
    text = models.TextField()
    likes = models.ManyToManyField('account.User', blank=True, related_name='liked_comment')
    dislikes = models.ManyToManyField('account.User', blank=True, related_name='disliked_comment')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'
        ordering = ('-date',)

    def __str__(self):
        return self.text[0:10]