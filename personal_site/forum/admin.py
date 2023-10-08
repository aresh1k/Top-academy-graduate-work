from django.contrib import admin
from .models import Discussion, Comment


class DiscussionAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created')
    list_filter = ['created']
    readonly_fields = ('user', 'created')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('theme', 'user', 'created')
    list_filter = ['created']
    readonly_fields = ('user', 'theme', 'created')


admin.site.register(Discussion, DiscussionAdmin)
admin.site.register(Comment, CommentAdmin)
