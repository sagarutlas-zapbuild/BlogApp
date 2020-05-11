from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework import viewsets
""" from .serializers import LoginSerializer """
from django.contrib.auth.backends import BaseBackend
from rest_framework import status
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model
UserModel = get_user_model()

"""
        {"username":"sagar@zapbuild.com","password":"password"}
        """
""" class LoginViewSet(viewsets.GenericViewSet):
    serializer_class = LoginSerializer

    def login(request):
        
        print(request.data)
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        print(user.groups.all())
        if user is not None:
            request.session['user_id'] = user.id
            return Response(status=status.HTTP_200_OK)
        else:
            return Response("Your username and password didn't match.", status=status.HTTP_400_BAD_REQUEST)


    def login(request):
        
        print(request.data)
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        print(user.groups.all())
        if user is not None:
            request.session['user_id'] = user.id
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response("Your username and password didn't match.", status=status.HTTP_403_FORBIDDEN)
 """


class BlogBackend(BaseBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            user = UserModel._default_manager.get_by_natural_key(username)
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            UserModel().set_password(password)
        else:
            if user.check_password(password) and user.is_active:
                return user
            elif not user.is_active:
                return ("User is inactive. Contact Administration.")

    def get_user(self, user_id):
        try:
            user = UserModel._default_manager.get(pk=user_id)
        except UserModel.DoesNotExist:
            user = AnonymousUser()
            return user
        return user if self.user_can_authenticate(user) else None

    def get_all_permissions(self, user_obj, obj=None):
        if not user_obj.is_active or user_obj.is_anonymous:
            return {'view_post', 'add_user', 'view_user'}
        if not hasattr(user_obj, '_perm_cache'):
            user_obj._perm_cache = {
                *self.get_user_permissions(user_obj),
                *self.get_group_permissions(user_obj),
            }

    def has_perm(self, user_obj, perm, obj=None):
        if perm in ['view_post', 'add_user', 'view_user']:
            return True
        return user_obj.is_active and perm in self.get_all_permissions(user_obj, obj)
