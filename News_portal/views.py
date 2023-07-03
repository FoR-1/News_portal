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
    template_name = 'news_2.html'
    context_object_name = 'category'