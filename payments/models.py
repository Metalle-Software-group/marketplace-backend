from django.db import models
from accounts.models import CustomUser

from orders.models import Orders

# Create your models here.


class Payments(models.Model):
    initiated_on = models.DateTimeField(auto_now_add=True, null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=255, null=False)

    # relations
    order = models.ForeignKey(
        Orders,
        related_name="payments",
        on_delete=models.CASCADE
    )
    customer = models.ForeignKey(
        CustomUser,
        related_name="payments",
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = "payments"
