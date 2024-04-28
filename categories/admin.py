from django.contrib import admin

from categories.models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(Category, CategoryAdmin)