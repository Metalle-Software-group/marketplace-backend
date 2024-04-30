from django.contrib import admin

from products.models import Attributes, Product

# Register your models here.
class AdminModel(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'created_at', 'updated_at', 'owner']


class AttributeAdminModel(admin.ModelAdmin):
    list_display = ['attribute', 'value']


admin.site.register(Attributes, AttributeAdminModel)

admin.site.register(Product, AdminModel)
