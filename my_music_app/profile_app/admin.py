from django.contrib import admin

# Register your models here.
from my_music_app.profile_app.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "age")


admin.site.register(Profile, ProfileAdmin)