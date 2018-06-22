from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from .models import Post

# def index(request):
#     return redirect('posts:post_list')

def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts,
    }
    return render(request, 'posts/post_list.html', context)

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post' : post,
    }
    return render(request, 'posts/post_detail.html', context)
