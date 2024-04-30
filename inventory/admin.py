from django.contrib import admin

from inventory.models import InventoryItem

# Register your models here.
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ["cost", "quantity", "vendor", "product", "units"]

admin.site.register(InventoryItem, InventoryItemAdmin)