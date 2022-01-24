from django.shortcuts import render, get_object_or_404
from .models import Post, Group

AMOUNT_ON_PAGE = 10


def index(request):
    posts = Post.objects.order_by('-pub_date')[:AMOUNT_ON_PAGE]
    template = 'posts/index.html'
    title = 'Главная страница'
    context = {
        'title': title,
        'posts': posts,
        'text': 'Это главная страница проекта Yatube'
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.groups.order_by('-pub_date')[:AMOUNT_ON_PAGE]
    title = 'Записи группы'
    context = {
        'group': group,
        'posts': posts,
        'title': title
    }
    return render(request, 'posts/group_list.html', context)
