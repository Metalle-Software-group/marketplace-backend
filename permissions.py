from django.contrib.auth.models import Group

admin_group, created = Group.objects.get_or_create(name='Admins')
customer_group, created = Group.objects.get_or_create(name='Customers')
vendor_group, created = Group.objects.get_or_create(name='Vendors')