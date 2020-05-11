from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.decorators import api_view, authentication_classes, permission_classes, action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from .models import User, Post, Comment, Category, PostCategory, Tag, PostTag
from .serializers import UserSerializer, PostSerializer, CommentSerializer, CategorySerializer, PostCategorySerializer, TagSerializer, PostTagSerializer

from .backends import authenticate

# Create your views here.


""" class AccountsViewset(viewsets.GenericViewSet):
    permission_required=[] """


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
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


@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def PostList(request):
    return Response(Post.objects.filter(published=True).values('id', 'author', 'title', 'summary'))


@action(methods=['post'], detail=True, permission_classes=['add_post'])
def PostCreate(self, request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewset(viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):

        user = User.objects.get(pk=pk)
        data = {}
        data['id'] = user.id
        data['name'] = user.name
        data['email'] = user.email
        data['intro'] = user.intro
        data['profile'] = user.profile
        return Response(data, status=status.HTTP_302_FOUND)


class PostViewset(viewsets.GenericViewSet):

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def retrieve(self, request, pk):
        post = Post.objects.get(pk=pk)
        data = {}
        data['title'] = post.title
        data['content'] = post.content
        data['updated_at'] = post.updated_at
        data['author'] = post.author.email
        data['author_intro'] = post.author.intro
        if (post.parent):
            data['parent_id'] = post.parent.id
            data['parent_title'] = post.parent.title
        return Response(data, status=status.HTTP_302_FOUND)

    @permission_classes([AllowAny])
    def list(self, request):
        return Response(Post.objects.filter(published=True).values('id', 'author', 'title', 'summary'))


class CommentViewset(viewsets.GenericViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CategoryViewset(viewsets.GenericViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class PostCategoryViewset(viewsets.GenericViewSet):
    serializer_class = PostCategorySerializer
    queryset = PostCategory.objects.all()


class TagViewset(viewsets.GenericViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class PostTagViewset(viewsets.GenericViewSet):
    serializer_class = PostTagSerializer
    queryset = PostTag.objects.all()
