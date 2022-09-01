from rest_framework import serializers, validators
from .models import Cal, CalPermissionTable


# Calendar Serializers
class BaseCalSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        model = Cal
        lookup_field = 'uuid'
        validators = [
            validators.UniqueTogetherValidator(queryset=Cal.objects.all(), fields=['owner'])]

class FullCalSerializer(BaseCalSerializer):
    class Meta(BaseCalSerializer.Meta):
        fields = [
            'id',
            'uuid',
            'owner',
            'owner_class',
            'icalURL',
        ]

class BasicCalSerializer(BaseCalSerializer):
    class Meta(BaseCalSerializer.Meta):
        fields = [
            'uuid',
            'owner',
            'owner_class',
            'icalURL',
        ]
        extra_kwargs = {
            'owner': {
                'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault()),
        }}


# Permission table Serializer
class CalPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalPermissionTable
        fields = [
            'cal_uuid',
            'user_uuid',
        ]
        validators = [
            validators.UniqueTogetherValidator(
                queryset=CalPermissionTable.objects.all(),
                fields=['cal_uuid', 'user_uuid']
            )
        ]