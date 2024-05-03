from django.contrib import admin

from units.models import Unit

# Register your models here.
class UnitsAdmin(admin.ModelAdmin):
    list_display = ["UOM_name", "UOM_abbr", "UOM_description", "Base_unit", "UOM_conversion_factor"]

    def __str__(self):
        return self.UOM_name

    def __repr__(self):
        return self.UOM_name


admin.site.register(Unit, UnitsAdmin)