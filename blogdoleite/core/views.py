from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-date_published')
    data = {
        'post_list': posts,
    }
    return render(request, 'core/index.html',data) #busca o arquivo index.html dentro do diretório templates/core/index.html.

def detail(request, id): #id é a variável que irá filtrar o post
    post = Post.objects.get(id = id)
    data = {
        'post': post
    }
    return render(request, 'core/detail.html', data)