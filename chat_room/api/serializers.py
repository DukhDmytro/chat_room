import re
from chat_room.models import Messages
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):
    """
    Serializer for Messages model
    """
    class Meta:
        model = Messages
        fields = 'message', 'author', 'email', 'create_date', 'update_date', 'id'

    def validate_email(self, email):
        """Email validator"""
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if re.match(regex, email):
            return email
        raise serializers.ValidationError('Invalid email')


    def validate_message(self, message):
        """Message validation"""
        regex = '^.{1,100}$'
        if re.fullmatch(regex, message):
            return message
        raise serializers.ValidationError('Message must contain 1-100 chars')
