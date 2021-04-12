from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'image_tag', 'date', 'text','pk')
    search_fields = ('text','user__username')


admin.site.register(Post, PostAdmin)
