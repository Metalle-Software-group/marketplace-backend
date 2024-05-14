from django.contrib import admin

from products.models import Product

# Register your models here.
class AdminModel(admin.ModelAdmin):
    list_display = ['name', 'description', 'brand', 'created_at', 'updated_at', 'vendor', "unit"]

    class Meta:
        model = Product

admin.site.register(Product, AdminModel)
