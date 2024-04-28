from rest_framework import serializers

from units.models import Unit

class UnitSerializer(serializers.ModelSerializer):
    # created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Unit
        fields = "__all__"

        # exclude = ["created_by", "created_on"]
