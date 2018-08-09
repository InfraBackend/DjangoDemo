from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from . import views
from .utils import download

urlpatterns = [
    # path('users', ProfileListView.as_view({'get':'list',})),
    path('authorizations', obtain_jwt_token),
    path('download', download),
    # path('dis/<int:pk>', views.DistributionView.as_view())
    ]

router = DefaultRouter()
router.register('users',views.ProfileViewSet, base_name='users')
# router.register('act',views.UserViewSet)
urlpatterns += router.urls