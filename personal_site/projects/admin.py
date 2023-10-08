from django.contrib import admin
from .models import Project, Article
from django.utils.safestring import mark_safe


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image', 'created')
    readonly_fields = ('created', 'get_image')

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width='200'")

    get_image.short_description = 'Изображение'


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image', 'created')
    readonly_fields = ('created', 'get_image')

    def get_image(self, obj):
        if obj.preview_image:
            return mark_safe(f"<img src='{obj.preview_image.url}' width='200'")

    get_image.short_description = 'Изображение'


admin.site.register(Project, ProjectAdmin)
admin.site.register(Article, ArticleAdmin)
