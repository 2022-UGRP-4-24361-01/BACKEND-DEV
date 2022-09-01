from .models import User
from rest_framework import serializers

class BaseUserSerializer(serializers.ModelSerializer):
    pw_1 = serializers.CharField(write_only=True)
    pw_2 = serializers.CharField(write_only=True)
    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            username = validated_data['username'],
            password = validated_data['password']
        )
        return user
    def validate(self, data):
        if data['pw_1'] != data['pw_2']:
            raise serializers.ValidationError("password not equal")
        data['password'] = data['pw_1']
        return data

    class Meta:
        abastract = True
        model = User
        lookup_field = 'uuid'


class FullUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = [
            'id',
            'uuid',
            'email',
            'username',
            'pw_1',
            'pw_2',
        ]


class BasicUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = [
            'uuid',
            'email',
            'username',
            'pw_1',
            'pw_2',
        ]
