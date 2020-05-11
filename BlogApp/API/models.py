from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from .managers import UserManager
# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=300)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    """ The brief introduction of the Author to be displayed on each post. """
    intro = models.CharField(max_length=100, null=True, default=None)
    """ The author details to be displayed on the Author Page. """
    profile = models.TextField(null=True, default=None)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.name + " (" + self.email + ")"


class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, to_field='email')
    parent = models.ForeignKey("Post", on_delete=models.DO_NOTHING, null=True)
    title = models.CharField(max_length=100)
    """ The meta title to be used for browser title and SEO. """
    meta_title = models.CharField(max_length=150, null=True, blank=True)
    """ The post slug to form the URL. """
    slug = models.CharField(max_length=100, null=True, blank=True)
    summary = models.CharField(null=True, blank=True, max_length=103)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True)
    content = models.TextField()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey("Comment", on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True)
    content = models.TextField()


class Category(models.Model):
    parent = models.ForeignKey("Category", on_delete=models.CASCADE)
    title = models.CharField(max_length=75)
    meta_title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    content = models.TextField()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Tag(models.Model):
    title = models.CharField(max_length=75)
    meta_title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    content = models.TextField()


class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
