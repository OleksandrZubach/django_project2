# from .views import *
# from django.urls import path
# app_name = "blog_app"
# urlpatterns = [
#     path('posts/', BlogListView.as_view(), name='posts'),
#     path('post/<int:pk>', BlogDetailView.as_view(), name='post'),
#     path('post_delete/<int:pk>', BlogDeleteView.as_view(), name='delete_post'),
#     path('update_post/<int:pk>', BlogUpdateView.as_view(), name='update_post'),
#     path('create_post/', BlogPostCreateView.as_view(), name='create_post'),
#     path('post/<int:year>/<int:month>/<int:day>/<slug:slug_id>', BlogDetailView.as_view(), name='post_by_slug'),
# ]



#     path('posts/', BlogListView.as_view(), name='posts'),
#     path('post/<int:pk>/', BlogDetailView.as_view(), name='post'),
#     path('post/<int:year>/<int:month>/<int:day>/<slug:slug_id>/', BlogDetailView.as_view(), name='post_by_slug'),
#     path('create_post/', BlogPostCreateView.as_view(), name='create_post'),
#     path('update_post/<int:pk>/', BlogUpdateView.as_view(), name='update_post'),
#     path('delete_post/<int:pk>/', BlogDeleteView.as_view(), name='delete_post'),
#     path('', PostListView.as_view(), name='blogpost_list'),
#     path('posts/', BlogListView.as_view(), name='post_list'),
#     path('posts/drafts/', BlogListView.as_view(), {'status': 'draft'}, name='draft_posts'),
#     path('posts/published/', BlogListView.as_view(), {'status': 'published'}, name='published_posts'),
#     path('posts/', BlogListView.as_view(), name='post_list'),
#     path('user/<str:username>/', BlogListView.as_view(), name='user_posts'),  # Пости конкретного користувача
#     path('published/', BlogListView.as_view(), name='published_posts'),  # Опубліковані пости для поточного користувача
#     path('draft/', BlogListView.as_view(), name='draft_posts'),  # Чернетки для поточного користувача
#     path('', BlogListView.as_view(), name='posts'),
# path('posts/<str:status>/', BlogListView.as_view(), name='blog_list_status'),
#     path('posts/', BlogListView.as_view(), name='blog_list'),
from .views import *
from django.urls import path

app_name = "blog_app"

urlpatterns = [
    path('posts/', BlogListView.as_view(), name='posts'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post'),
    path('post/<int:year>/<int:month>/<int:day>/<slug:slug_id>/', BlogDetailView.as_view(), name='post_by_slug'),
    path('create_post/', BlogPostCreateView.as_view(), name='create_post'),
    path('update_post/<int:pk>/', BlogUpdateView.as_view(), name='update_post'),
    path('delete_post/<int:pk>/', BlogDeleteView.as_view(), name='delete_post'),
    path('posts/drafts/', BlogListView.as_view(), {'status': 'draft'}, name='draft_posts'),
    path('posts/published/', BlogListView.as_view(), {'status': 'published'}, name='published_posts'),
    path('user/<str:username>/', BlogListView.as_view(), name='user_posts'),
    path('', BlogListView.as_view(), name='posts'),
    path('<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('create/', BlogPostCreateView.as_view(), name='create_post'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('published/', BlogListView.as_view(), {'status': 'published'}, name='published_posts'),
    path('draft/',BlogListView.as_view(), {'status': 'draft'}, name='draft_posts'),
    path('published/', PublishedPostsView.as_view(), name='published_posts'),

    # Шлях до неопублікованих постів
    path('unpublished/', UnpublishedPostsView.as_view(), name='unpublished_posts'),

]





# urlpatterns = [
#     path('posts/', BlogListView.as_view(), name='posts'),
#     path('post/<int:pk>/', BlogDetailView.as_view(), name='post'),
#     path('post/<int:year>/<int:month>/<int:day>/<slug:slug_id>/', BlogDetailView.as_view(), name='post_by_slug'),
#     path('create_post/', BlogPostCreateView.as_view(), name='create_post'),
#     path('update_post/<int:pk>/', BlogUpdateView.as_view(), name='update_post'),
#     path('delete_post/<int:pk>/', BlogDeleteView.as_view(), name='delete_post'),
#     path('', PostListView.as_view(), name='blogpost_list'),
#     path('posts/', BlogListView.as_view(), name='post_list'),
#     path('posts/drafts/', BlogListView.as_view(), {'status': 'D'}, name='draft_posts'),
#     path('posts/published/', BlogListView.as_view(), {'status': 'P'}, name='published_posts'),
# ]


# from .views import *
# from django.urls import path
#
# app_name = "blog_app"
#
#
# urlpatterns = [
#
#     path('posts/<str:status>/', BlogListView.as_view(), name='post_list_by_status'),  # Фільтрація постів за статусом
#     path('post/<int:pk>/', BlogDetailView.as_view(), name='post'),
#     path('create_post/', BlogPostCreateView.as_view(), name='create_post'),
#     path('update_post/<int:pk>/', BlogUpdateView.as_view(), name='update_post'),
#     path('delete_post/<int:pk>/', BlogDeleteView.as_view(), name='delete_post'),
# path('posts/', BlogListView.as_view(), name='post_list'),  # Для всіх постів
#     path('posts/published/', BlogListView.as_view(), {'status': 'published'}, name='published_posts'),  # Для опублікованих постів
#     path('posts/drafts/', BlogListView.as_view(), {'status': 'draft'}, name='draft_posts'),  # Для неопублікованих постів
# ]