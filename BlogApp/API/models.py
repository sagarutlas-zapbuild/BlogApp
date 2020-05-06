from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group
from django.utils.translation import gettext_lazy as _
# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('groups','users')
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)   
    password = models.CharField(max_length=300)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    """ The brief introduction of the Author to be displayed on each post. """
    intro = models.CharField(max_length=100, null=True)
    """ The author details to be displayed on the Author Page. """
    profile = models.TextField(null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    objects = UserManager()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey("Post", on_delete=models.DO_NOTHING, null=True)
    title = models.CharField(max_length=100)
    """ The meta title to be used for browser title and SEO. """
    meta_title = models.CharField(max_length=150, null=True)
    """ The post slug to form the URL. """
    slug = models.CharField(max_length=100, null=True)
    summary = models.TextField(null=True)
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
