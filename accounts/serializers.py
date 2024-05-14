from django.contrib.auth.hashers import make_password
from accounts.models import CustomUser, Vendor
from marketplace.roles import VENDOR_ROLE
from django.contrib.auth.models import Group
from rest_framework import serializers
from django.db import transaction

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    def create(self, validated_data):
        validated_data.update({"password": make_password(
            validated_data.get("password")
            )
        })

        return super().create(
            validated_data
        )

    class Meta:
        model = CustomUser
        exclude = ["is_staff", "is_superuser", "groups", "user_permissions","date_joined"]

class VendorSerializer(serializers.ModelSerializer):
    user = UserSerializer(many = False)

    class Meta:
        model = Vendor
        fields = ["user", "company_name", "address", "phone", "id", "company_website"]


class VendorCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    user = UserSerializer(required = True)

    def create(self, validated_data):
        with transaction.atomic():
            user_data = validated_data.pop("user")
            user_serializer = UserSerializer(
                data = {
                    **user_data,
                    "is_active": False
                    }
            )

            user_serializer.is_valid(raise_exception=True)
            user = user_serializer.save()

            vendor_group, _ = Group.objects.get_or_create(
                name = VENDOR_ROLE
                )

            user.groups.add(vendor_group)

            return Vendor.objects.create(user = user, **validated_data)

    class Meta:
        fields = ["user", "company_name", "address", "phone", "id"]
        model = Vendor