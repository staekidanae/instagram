from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect


def index(request):
    return redirect('posts:post_list')