from rest_framework.authentication import BaseAuthetication
from django.contrib.auth.models import User


class CustomAuthentication(BaseAuthetication):
    def authenticate(self, request,username,password):
        try:
            user=User.objects.get(email=username)
            success=user.check_password(password)
            if success:
                return user

        except User.DoesNotExist:
            pass
        return None


    def get_user(self, uid):
        try:
            user = User.objects.get(id=uid)

        except:
            None
