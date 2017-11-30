from rest_framework import serializers
from rest_app_photo_book.models import User

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')