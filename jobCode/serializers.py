from rest_framework import serializers
from rest_framework import serializers
from jobCode.model.location import LocationModel  
from jobCode.model.logger import LoggerModel

class VersionSerializer(serializers.Serializer):
    version = serializers.CharField(read_only=True)

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationModel
        fields = '__all__'

class LoggerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoggerModel
        fields = '__all__'  