from rest_framework import serializers
from .models import Cal, Small

class SmallSerializer(serializers.ModelSerializer):
    s1 = serializers.CharField()
    s2 = serializers.CharField()
    # class Meta:
    #     model = Small
    #     fields = '__all__'

class CalSerializer(serializers.ModelSerializer):
    s_id_asdf = SmallSerializer()
    var1 = serializers.CharField()
    var2 = serializers.CharField()
    var3 = serializers.CharField()
    # class Meta:
    #     model = Cal
    #     fields = '__all__'