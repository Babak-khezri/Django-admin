from django.db import models
from account.models import User

# Create your models here.


class FileMessage(models.Model):
    file = models.FileField(upload_to='chat/files')



class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chats")
    getter = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(default="")
    date = models.DateTimeField(auto_now_add=True, editable=False)
    seen = models.BooleanField(default=False)
    file = models.OneToOneField(FileMessage, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'

    def __str__(self):
        return self.text[0:3]
