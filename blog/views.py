from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def all_blogs(request):
    blogs = Blog.objects.all()

    # Отсортировать по дате и выдать последние свежие статьи из блога кол-ом 5шт
    # blogs = Blog.objects.order_by('-date')[:5]

    return render(request, 'blog/all_blogs.html', {'blogs': blogs})

def detail(request, blog_id):
    # Вернем отдельный объект из БД, исп-я id из urls.py в перемнное block_id
    # в противном случае будет ошибка 404 если нет номера с таким id
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
