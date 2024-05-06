from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class Meta:
        db_table = "users"

    def __str__(self):
        return self.username

    def __repr__(self):
        return self.username

    def __str__(self):
        return self.email

    def __repr__(self):
        return self.email


class Vendor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='vendor')

    company_name = models.CharField(max_length=100, null=False)
    company_website = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.company_name

    def __repr__(self):
        return self.company_name

    class Meta:
        db_table = "vendors"

    def __str__(self):
        return self.company_name

    def __repr__(self):
        return self.company_name
