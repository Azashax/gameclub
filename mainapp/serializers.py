from django.db.models import fields
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from .models import *


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class GamerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gamer
        fields = '__all__'


class RentedDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentedDevice
        fields = '__all__'



class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = '__all__'


# class Book1CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BookCategory
#         fields = '__all__'
#
#
# class profil(WritableNestedModelSerializer):
#     BookCategory = BookCategorySerializer(many=True)
#     Book1Category = Book1CategorySerializer(many=True)
#
#     class Meta:
#         model = Profile
#         fields = ('pk', 'BookCategory', 'Book1Category', 'AccessKey')
#
#
# class AccessKeySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AccessKey
#         fields = ('pk', 'key',)