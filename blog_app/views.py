from django.shortcuts import render, get_object_or_404, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import BlogPost
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from .models import BlogPost, Comment
from .forms import CommentForm

class PublishedPostsView(ListView):
    model = BlogPost
    template_name = 'blog_app/blogpost_list.html'  # Шаблон для відображення публікацій
    context_object_name = 'blogpost_list'
    paginate_by = 6  # Кількість постів на сторінці

    def get_queryset(self):
        # Фільтруємо пости за статусом "опубліковано"
        return BlogPost.objects.filter(status=BlogPost.Status.PUBLISHED)

class UnpublishedPostsView(ListView):
    model = BlogPost
    template_name = 'blog_app/blogpost_list.html'  # Шаблон для відображення чернеток
    context_object_name = 'blogpost_list'
    paginate_by = 6  # Кількість постів на сторінці

    def get_queryset(self):
        # Фільтруємо пости за статусом "чернетка"
        return BlogPost.objects.filter(status=BlogPost.Status.DRAFT)



class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blogpost_confirm_delete.html'
    success_url = reverse_lazy('blog_app:post_list')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)

# class BlogListView(ListView):
#     model = BlogPost
#     paginate_by = 6
#     model=BlogPost
#     queryset = BlogPost.published_objects.all()
#     context_object_name = 'blogpost_list'

class BlogListView(ListView):
    model = BlogPost
    paginate_by = 6
    context_object_name = 'blogpost_list'

    # def get_queryset(self):
    #     status = self.kwargs.get('status', None)  # Отримуємо параметр статус
    #     if status == 'published':
    #         return BlogPost.objects.filter(status=BlogPost.Status.PUBLISHED)
    #     elif status == 'draft':
    #         return BlogPost.objects.filter(status=BlogPost.Status.DRAFT)
    #     return BlogPost.objects.all()
    def get_queryset(self):
        status = self.kwargs.get('status', None)
        username = self.kwargs.get('username', None)  # Отримуємо username з URL
        queryset = BlogPost.objects.all()

        if username:
            queryset = queryset.filter(owner__username=username)  # Фільтруємо по користувачу

        if status == 'published':
            queryset = queryset.filter(status=BlogPost.Status.PUBLISHED)
        elif status == 'draft':
            queryset = queryset.filter(status=BlogPost.Status.DRAFT)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        status = self.kwargs.get('status', None)
        context['status'] = status  # Додаємо статус до контексту
        return context

# class BlogListView(ListView):
#     model = BlogPost
#     template_name = 'blogapp_list.html'
#     context_object_name = 'blogpost_list'
#     paginate_by = 6
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user_model = get_user_model()
#         context['user_model'] = user_model
#         return context


class PostListView(ListView):
    model = BlogPost
    template_name = 'blog_app/blogpost_list.html'
    context_object_name = 'blogpost_list'

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog_app/blogpost_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()  # Передаємо форму в контекст
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('blog_app:post_detail', pk=post.pk)  # Перенаправлення після успішного збереження коментаря

        # Якщо форма не валідна, передаємо її з помилками
        context = self.get_context_data(object=self.get_object())
        context['comment_form'] = form  # Передаємо форму з помилками
        return self.render_to_response(context)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    success_url = reverse_lazy("blog_app:posts")
    fields = ["title", "text", "status"]
    login_url = '/login/'  # URL сторінки для входу

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    success_url = reverse_lazy("blog_app:posts")
    login_url = '/login/'

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)


class BlogPostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    fields = ["title", "text", "status"]
    template_name = 'blog_app/blogpost_create_post.html'
    login_url = '/login/'

    def form_valid(self, form):
        print('form_valid called')
        obj = form.save(commit=False)
        obj.owner = self.request.user
        if obj.status == BlogPost.PUBLISHED and not obj.published_at:
            obj.published_at = timezone.now()
        obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog_app:posts')








# ************************************************************************

# class MyPostsListView(ListView):
#     model = BlogPost
#     paginate_by = 5
#     queryset = BlogPost.objects.all()
#
#     def get_queryset(self, **kwargs):
#         qs = BlogPost.objects.filter(owner = self.request.user)
#         return qs
#
