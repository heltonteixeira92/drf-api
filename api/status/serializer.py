from rest_framework import serializers

from user.serializer import UserSerializer
from .services import StatusDataClass


class StatusSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    content = serializers.CharField()
    data_published = serializers.CharField()
    user_id = UserSerializer(read_only=True)

    def to_internal_value(self, data):
        """to_internal_value() allows us to change the deserialization output"""

        data = super().to_internal_value(data)

        return StatusDataClass(**data)
