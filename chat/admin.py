from django.contrib import admin
from .models import Message,FileMessage
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender','getter','text','seen']

admin.site.register(Message,MessageAdmin)
admin.site.register(FileMessage)