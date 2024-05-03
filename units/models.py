from django.db import models

from accounts.models import CustomUser

# Create your models here.

class Unit(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null = False)
    UOM_description = models.CharField(max_length=100, null=False)
    Base_unit = models.BooleanField(default = False, null = False)
    UOM_conversion_factor = models.IntegerField(null=False)
    UOM_name = models.CharField(max_length=100, null=False)
    UOM_abbr = models.CharField(max_length=10, null=False)

    # relations
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        db_table = "units"
        unique_together = ("UOM_name", "UOM_abbr")

    def __str__(self):
        return self.UOM_name

    def __repr__(self):
        return self.UOM_name
