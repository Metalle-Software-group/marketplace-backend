from rest_framework import serializers

from units.models import Unit

class UnitSerializer(serializers.ModelSerializer):
    # created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Unit
        exclude = ["created_on", "created_by"]

        # exclude = ["created_by", "created_on"]
