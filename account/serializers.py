from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            username = validated_data['username'],
            password = validated_data['password']
        )
        return user
    class Meta:
        model = User
        lookup_field = 'uuid'
        fields = [
            'id', # only for admin
            'uuid',
            'email',
            'username',
            'password',
        ]