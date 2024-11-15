from .views import *
from django.urls import path
app_name = "blog_app"
urlpatterns = [
    path('posts/', BlogListView.as_view(), name='posts'),
    path('post/<int:pk>', BlogDetailView.as_view(), name='post'),
    path('post_delete/<int:pk>', BlogDeleteView.as_view(), name='delete_post'),
    path('update_post/<int:pk>', BlogUpdateView.as_view(), name='update_post'),
    path('create_post/', BlogPostCreateView.as_view(), name='create_post'),
    path('post/<int:year>/<int:month>/<int:day>/<slug:slug_id>', BlogDetailView.as_view(), name='post_by_slug'),


]