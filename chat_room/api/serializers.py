from chat_room.models import Messages
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):
    """
    Serializer for Messages model
    """
    class Meta:
        model = Messages
        fields = 'message', 'author', 'email', 'create_date', 'update_date', 'id'
