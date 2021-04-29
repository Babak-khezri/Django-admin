from django.contrib import admin
from .models import Story, Highlight
# Register your models here.

def make_active_story(modeladmin, request, queryset):
    queryset.update(status='a')
    queryset.update(date="")
    modeladmin.message_user(request, 'مقالات منتشر شدند')


class StoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'image_tag', 'status', 'hits_count')
    list_filter = (['user', 'status'])
    ordering = ('-date',)
    actions = [make_active_story]


class HighlightAdmin(admin.ModelAdmin):
    list_display = ('name','user', 'image_tag',  'stories_count')
    list_filter = (['user'])


admin.site.register(Story, StoryAdmin)
admin.site.register(Highlight, HighlightAdmin)
