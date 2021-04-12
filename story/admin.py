from django.contrib import admin
from .models import Story, Highlight
# Register your models here.


class StoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'image_tag', 'status', 'hits_count')
    list_filter = (['user', 'status'])
    ordering = ('-date',)


class HighlightAdmin(admin.ModelAdmin):
    list_display = ('name','user', 'image_tag',  'stories_count')
    list_filter = (['user'])


admin.site.register(Story, StoryAdmin)
admin.site.register(Highlight, HighlightAdmin)
