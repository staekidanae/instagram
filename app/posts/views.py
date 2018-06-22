from django.http import HttpResponse, request
from django.shortcuts import render
from .models import Post

def index():
    pass

def post_list(request):
    # poasts = Post.objects.all()
    # contextx = {
    #     'posts' : posts
    # }
    return render(request, 'posts/post_list.html')

def post_detail():
    return render(request, 'posts/post_detail.html')
