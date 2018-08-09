from rest_framework import serializers
from rest_framework.validators import UniqueValidator
import re

from .models import UserProfile

# class UserSerializer(serializers.ModelSerializer):
#     name = serializers.CharField(required=True, allow_blank=False,
#                                      label="用户名", max_length=30,
#     validators=[UniqueValidator(queryset=UserProfile.objects.all(),
#                                          message='用户已存在')])
#
#     class Meta:
#         model = UserProfile
#         fields = '__all__'
#
#
#     def validate_mobile(self, value):
#         """
#         验证手机号
#         """
#         if not re.match(r'^1[3-9]\d{9}$', value):
#             raise serializers.ValidationError('手机号格式错误')
#         return value
#
#     def update(self, instance, validated_data):
#         instance.save()
#         return instance
#
#     def create(self, validated_data):
#         user = super().create(validated_data)
#         return user

class UserSerializer(serializers.ModelSerializer):
        mobile = serializers.CharField(required=True, allow_blank=False,
                                         label="手机号", max_length=11,
        validators=[UniqueValidator(queryset=UserProfile.objects.all(),
                                             message='用户已存在')])
        class Meta:
            model = UserProfile
            fields = '__all__'



# class CreateUserSerializer(serializers.ModelSerializer):
#     """创建用户"""
#     token = serializers.CharField(read_only=True)
#     class Meta:
#         fields = '__all__'
#     def create(self, validated_data):
#         del validated_data['image_code']
#         user = super().create(validated_data)
