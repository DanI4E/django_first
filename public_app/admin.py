from django.contrib import admin
from .models import Post


# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'title', 'image')
    ordering = ('-id', '-created_at')
    readonly_fields = ('created_at',)
