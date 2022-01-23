from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Group

# Create your views here.

# Главная страница
def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    template = 'posts/index.html'
    title = 'Главная страница'
    context = {
        'title': title,
        'posts': posts,
        'text': 'Это главная страница проекта Yatube'
    }
    return render(request, template, context)

# Лента постов групп
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    title = 'Записи группы'
    context = {
        'group': group,
        'posts': posts,
        'title' : title
    }
    return render(request, 'posts/group_list.html', context)