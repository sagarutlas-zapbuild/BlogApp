from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Post, Comment, Category, PostCategory, Tag, PostTag
from .serializers import UserSerializer, PostSerializer, CommentSerializer, CategorySerializer, PostCategorySerializer, TagSerializer, PostTagSerializer
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from django.contrib.auth import authenticate
# Create your views here.

@api_view(['POST'])
def login(request):
    """
    {
        "username":"sagar@zapbuild.com",
        "password":"password"
    }
    """
    username = request.data['username']
    password = request.data['password']
    user = authenticate(username=username, password=password)
    print(user.groups.all())
    if user is not None:
        request.session['member_id'] = user.id
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response("Your username and password didn't match.", status = status.HTTP_403_FORBIDDEN)

class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class PostViewset(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CommentViewset(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CategoryViewset(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class PostCategoryViewset(viewsets.ModelViewSet):
    serializer_class = PostCategorySerializer
    queryset = PostCategory.objects.all()


class TagViewset(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class PostTagViewset(viewsets.ModelViewSet):
    serializer_class = PostTagSerializer
    queryset = PostTag.objects.all()
