from django.contrib import admin
from .models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'image_tag', 'name', 'email', 'is_private')
    search_fields = ('username', 'email', 'name')
    list_filter = (['is_private', 'gender'])
    ordering = ('username',)


admin.site.register(User, UserAdmin)
