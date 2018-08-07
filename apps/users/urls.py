from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from .views import ProfileViewSet

urlpatterns = [
    # path('users', ProfileListView.as_view({'get':'list',})),
    path('authorizations', obtain_jwt_token),
    ]

router = DefaultRouter()
router.register('users',ProfileViewSet, base_name='users')
urlpatterns += router.urls