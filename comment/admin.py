from django.contrib import admin
from .models import Comment
# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'date')
    


admin.site.register(Comment,CommentAdmin)
