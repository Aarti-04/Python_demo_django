'''Email authentication'''
from typing import Any
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.http import HttpRequest
UserModel=get_user_model()
class EmailBackend(ModelBackend):
    '''Authenticate method override'''
    def authenticate(self, request: HttpRequest, email:str|None=..., password: str | None = ..., **kwargs: Any):
        try:
            user = UserModel.objects.get(email=email)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None
