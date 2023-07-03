from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import Category, Post


class CategoryList(ListView):
    model = Category
    ordering = 'name'
    template_name = 'news.html'
    context_object_name = 'categorys'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class CategoryDetail(DetailView):
    model = Category
    template_name = 'news.html'
    context_object_name = 'categorys'
    

class PostList(ListView):
    model = Post
    ordering = 'name'
    template_name = 'post.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'posts'