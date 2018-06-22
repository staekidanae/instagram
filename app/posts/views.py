from django.http import HttpResponse, request
from django.shortcuts import render

def index():
    pass

def post_list(request):
    return HttpResponse('Post List')

def post_detail():
    return HttpResponse('Post Detail pk: {}'.format(pk))
