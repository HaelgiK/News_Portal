from django.shortcuts import render
from datetime import datetime
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Post
from .filters import PostFilter
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import ValidationError


class PostList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, которое будет использоваться для сортировки объектов
    ordering = '-date_created'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10


    # def get_queryset(self):
    #     # Получаем обычный запрос
    #     queryset = super().get_queryset()
    #     # Используем наш класс фильтрации.
    #     # self.request.GET содержит объект QueryDict
    #     # Сохраняем нашу фильтрацию в объекте класса,
    #     # чтобы потом добавить в контекст и использовать в шаблоне.
    #     self.filterset = PostFilter(self.request.GET, queryset)
    #     # Возвращаем из функции отфильтрованный список товаров
    #     return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
#        context['filterset'] = self.filterset
        context['time_now'] = datetime.utcnow()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'


class SearchNews(ListView):
    model = Post
    ordering = '-date_created'
    template_name = 'search.html'
    context_object_name = 'news'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

# Добавляем новое представление для создания новостей.
class PostCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post')
    # Указываем разработанную форму
    form_class = PostForm
    # модель новостей
    model = Post
    # новый шаблон, в котором используется форма.
    template_name = 'news_edit.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if 'article' in self.request.path:
            type_post = 'AR'
        else:
            type_post = 'NW'
        self.object.type_post = type_post
        return super().form_valid(form)

class NewsUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post')
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post')
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('post_detail')


class ArticleUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post')
    form_class = PostForm
    model = Post
    template_name = 'article_edit.html'


class ArticleDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post')
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('post_list')
