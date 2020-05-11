from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import login, UserViewset, PostViewset, CommentViewset, CategoryViewset, PostCategoryViewset, TagViewset, PostTagViewset

router = DefaultRouter()
router.register(r'users', UserViewset, basename='user')
router.register(r'posts', PostViewset, basename='post')
router.register(r'comments', CommentViewset, basename='comment')
router.register(r'categories', CategoryViewset, basename='category')
router.register(r'post_categories', PostCategoryViewset,
                basename='post_category')
router.register(r'tags', TagViewset, basename='tag')
router.register(r'post_tags', PostTagViewset, basename='post_tag')

urlpatterns = [path('', include(router.urls)), ]
