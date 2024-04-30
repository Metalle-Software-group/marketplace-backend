from django.db import models

from accounts.models import CustomUser

# Create your models here.

class Unit(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null = False)
    name = models.CharField(max_length=100, null=False)
    abbr = models.CharField(max_length=10, null=False)

    # relations
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        db_table = "units"

    def __str__(self):
        return self.unit