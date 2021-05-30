from django.contrib import admin
from .models import Comment
# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','text', 'date','likes_count','dislikes_count')
    


admin.site.register(Comment,CommentAdmin)
