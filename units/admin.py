from django.contrib import admin

from units.models import Unit

# Register your models here.
class UnitsAdmin(admin.ModelAdmin):
    list_display = ["name", "abbr"]

admin.site.register(Unit, UnitsAdmin)