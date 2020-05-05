from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


class User(AbstractBaseUser):
    name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=300)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    intro = models.CharField(max_length=100)
    profile = models.TextField()
    is_staff = models.BooleanField()
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)


class Post(models.Model):
    author
    parent
    title
    meta_title
    slug
    summary
    published
    created_at
    updated_at
    published_at
    content


class Comment(models.Model):
    user
    post
    parent
    title
    published
    created_at
    published_at
    content


class Category(models.Model):
    parent
    title
    meta_title
    slug
    content


class PostCategory(models.Model):
    post
    category


class Tag(models.Model):
    title
    meta_title
    slug
    content


class PostTag(models.Model):
    post
    tag
