from django.contrib.auth.backends import ModelBackend

from .models import UserProfile

def jwt_response_payload_handler(token, user=None, request=None):
    """自定义jwt认证成功后返回的数据"""
    return {
        'token':token,
        'user_id':user.id,
        'username':user.name
    }

class UsernameModelAuthBackend(ModelBackend):
    """自定义认证"""

    def authenticate(self, request, username=None, password=None, **kwargs):
        user = UserProfile.objects.get(username)
        if user is not None and user.check_password(password):
            return user