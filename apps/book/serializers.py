from rest_framework import serializers

from .models import BookInfo,HeroInfo

class BookModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookInfo
        fields = '__all__'

class HeroModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroInfo
        fields = '__all__'