from django.contrib import admin

from accounts.models import CustomUser

# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "first_name", "last_name"]

admin.site.register(CustomUser, CustomUserAdmin)