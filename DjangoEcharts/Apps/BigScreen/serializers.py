from rest_framework import serializers
from .models import BigScreen
from .models import UploadFile


class BigScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = BigScreen
        fields = '__all__'


class FileUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = UploadFile
        fields = ('id', 'file', 'created_at')

