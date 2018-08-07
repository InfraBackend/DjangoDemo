from django.shortcuts import render
from rest_framework import views,viewsets
from rest_framework import generics
from rest_framework import mixins
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .models import HeroInfo,BookInfo
from .serializers import BookModelSerializer,HeroModelSerializer


# APIView
class BooksAPIView(views.APIView):
    def get(self, request):
        blist = BookInfo.objects.all()
        book_serializer = BookModelSerializer(blist, many=True)
        return Response(book_serializer.data)

    def post(self, request):
        data = request.data
        book_serializer = BookModelSerializer(data=data)
        if book_serializer.is_valid():
            book_serializer.save()
            book_serializer = BookModelSerializer(book)
            return Response(book_serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
#GenericAPIView
class BooksGeneriAPIView(generics.GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookModelSerializer
    def get(self, request):
        blist = self.get_queryset()
        #单个对象
        book = self.get_object()
        book_serializer = self.get_serializer(blist,many=True)
        return Response(book_serializer.data)

# mixin
# ListModelMixin
# CreateModelMixin
# DestroyModelMixin
# RetrieveModelMixin 查询一个
# UpdateModelMixin

#mixins.ListModelMixin+mixins.CreateModelMixin+generics.GenericAPIView=ListCreateAPIView

class BooksGenericAPIView(mixins.ListModelMixin, mixins.CreateModelMixin,
                          generics.GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookModelSerializer

    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)
# 使用mixin+GenericAPIView结合

#ViewSet
class BookModelViewSet(viewsets.ModelViewSet):
    queryset = BookInfo.objects.all
    serializer_class = BookModelSerializer
# viewset类
# GenericViewSet 继承自GenericAPIView

