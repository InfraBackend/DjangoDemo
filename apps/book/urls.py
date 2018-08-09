from rest_framework import routers
from django.urls import path

from . import views

#viewset
router = routers.DefaultRouter()
router.register('books', views.BookModelViewSet, base_name='books')

urlpatterns = [

]

urlpatterns += router.urls