from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.generics import mixins,ListAPIView,RetrieveAPIView
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from .models import UserProfile
from . import serializers

# Create your views here.

class UserPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 2


# class ProfileViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
#                      mixins.UpdateModelMixin,viewsets.GenericViewSet):
#     """用户列表数据"""
#     queryset = UserProfile.objects.all()
#     serializer_class = serializers.UserSerializer
#     pagination_class = UserPagination
#
#     def create(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)
#
#     def update(self, request, *args, **kwargs):
#         user = self.get_object()
#         serializer = serializers.UserSerializer(instance=user, data=request.data)
#         return Response(serializer.data)

class ProfileViewSet(viewsets.ModelViewSet):
    """用户列表增删改查"""
    serializer_class = serializers.UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('score', 'create_time')
    def get_queryset(self):
        return UserProfile.objects.all()

#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = UserProfile.objects.all()
#     serializer_class = serializers.UserSerializer
#     @action(methods=['get'],detail=True)
#     def read(self, request, pk):
#         print(1)
#         return Response(status=status.HTTP_200_OK)

# class DistributionView(APIView):
#     def get(self,request,pk):
#         user = UserProfile.objects.get(pk=pk)
#         serializer = serializers.UserSerializer(user)
#         return Response(serializer.data)
#     def put(self, request, pk):
#         data = request.data
#         serializer = serializers.UserSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)




