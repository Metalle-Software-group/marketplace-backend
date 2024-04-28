from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, unique = True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        db_table = "categories"