from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .models import BlogPost
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.shortcuts import get_object_or_404,Http404


class BlogListView(ListView):
    model = BlogPost


class BlogDetailView(DetailView):
    model = BlogPost


class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ["title", "text"]

    def get_queryset(self, **kwargs):
        qset = super().get_queryset(**kwargs)
        qset = qset.filter(owner=self.request.user)
        return qset


class BlogDeleteView(DeleteView, BlogUpdateView):
    model = BlogPost
    success_url = reverse_lazy("blog_app:posts")

    def get_queryset(self, **kwargs):
        qset = super().get_queryset(**kwargs)
        qset = qset.filter(owner=self.request.user)
        return qset


class BlogDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        pk = self.kwargs.get("pk")

        year = self.kwargs.get("year")
        month = self.kwargs.get("month")
        day = self.kwargs.get("day")
        slug_id = self.kwargs.get("slug_id")

        if pk:
            return get_object_or_404(self.model, pk=pk)
        elif slug_id:
            return get_object_or_404(self.model, created_at__year=year, created_at__month=month, created_at__day=day,
                                     slug=slug_id)
        else:
            raise Http404("No object found matching the provided criteria.")


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ["title", "text", ]
    template_name = 'blog_app/blogpost_create_post.html'

    def form_valid(self, form):
        print('form_valid called')
        object = form.save(commit=False)
        object.owner = self.request.user
        object.save()
        return super(BlogPostCreateView, self).form_valid(form)

    def get_queryset(self, **kwargs):
        qset = super().get_queryset(**kwargs)
        qset = qset.filter(owner=self.request.user)
        return qset

    def get_success_url(self):
        return reverse_lazy('blog_app:posts')



