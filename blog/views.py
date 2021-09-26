from django.shortcuts import render
from .models import Blog

# Create your views here.

def all_blogs(request):
    blogs = Blog.objects.all()

    # Отсортировать по дате и выдать последние свежие статьи из блога кол-ом 5шт
    # blogs = Blog.objects.order_by('-date')[:5]

    return render(request, 'blog/all_blogs.html', {'blogs': blogs})
