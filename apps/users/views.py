from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import mixins,ListAPIView,RetrieveAPIView
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import UserProfile
from . import serializers

# Create your views here.

class UserPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 2


class ProfileViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                     mixins.UpdateModelMixin,viewsets.GenericViewSet):
    """用户列表数据"""
    queryset = UserProfile.objects.all()
    serializer_class = serializers.UserSerializer
    pagination_class = UserPagination

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = serializers.UserSerializer(instance=user, data=request.data)
        return Response(serializer.data)




