from django.urls import include, path
from django.contrib import admin

urlpatterns =  [
    path('categories/', include('categories.routes')),
    path('payments/', include('payments.routes')),
    path('mechants/', include('mechants.routes')),
    path('inventory/', include('inventory.routes')),
    path('accounts/', include('accounts.routes')),
    path('products/', include('products.routes')),
    path('coupons/', include('coupons.routes')),
    path('reports/', include('reports.routes')),
    path('orders/', include('orders.routes')),
    path('units/', include('units.routes')),
    path('admin/', admin.site.urls)
    ]