from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'created',)

    def delete_queryset(self, request, queryset):
        for data in queryset:
            profile_data = data
            super().delete_queryset(request, queryset)
            Profile.objects.create(user=profile_data.user, profile_name=profile_data.profile_name)

    def delete_model(self, request, obj):
        profile_data = obj
        super().delete_model(request, obj)
        Profile.objects.create(user=profile_data.user, profile_name=profile_data.profile_name)


admin.site.register(Profile, ProfileAdmin)
