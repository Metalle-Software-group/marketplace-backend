from django.contrib.auth.hashers import make_password
from accounts.models import CustomUser, Vendor
from rest_framework import serializers

class VendorSerializer(serializers.ModelSerializer):
    user=serializers.RelatedField(read_only=True)
    class Meta:
        model = Vendor
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    vendor = VendorSerializer(read_only = True)


    def create(self, validated_data):
        validated_data.update({"password":make_password(validated_data.get("password"))})

        return super().create(
            validated_data
        )

    class Meta:
        model = CustomUser
        depth = 1
        exclude = ["is_staff", "is_superuser", "groups", "user_permissions","date_joined"]
