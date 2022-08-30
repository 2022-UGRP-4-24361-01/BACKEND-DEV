from rest_framework import serializers
from .models import Cal
from account.serializers import UserSerializer

class BaseCalSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    # uuid = serializers.UUIDField(format='hex_verbose')
    # owner = UserSerializer(read_only=True, default=serializers.CurrentUserDefault())
    # owner = serializers.ModelSerializer(read_only=True, default=serializers.CurrentUserDefault()) ## may not operate
    # icalURL = serializers.URLField(max_length=200, min_length=None, allow_blank=False)
    class Meta:
        abstract = True
        model = Cal
        lookup_field = 'uuid'

class FullCalSerializer(BaseCalSerializer):
    class Meta(BaseCalSerializer.Meta):
        fields = [
            'id',
            'uuid',
            'owner',
            'icalURL'
        ]

class BasicCalSerializer(BaseCalSerializer):
    class Meta(BaseCalSerializer.Meta):
        fields = [
            'uuid',
            'owner',
            'icalURL'
        ]
        extra_kwargs = {
            'owner': {'read_only': True, 'default': serializers.CurrentUserDefault()}}