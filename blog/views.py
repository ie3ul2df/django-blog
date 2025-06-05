from django.shortcuts import render
from django.views import generic
from .models import Post



# from django.http import HttpResponse

# def hello_blog(request):
#     return HttpResponse("Hello, blog!")



# Create your views here.
class PostList(generic.ListView):
    # model = Post
    # queryset = Post.objects.all()
    # queryset = Post.objects.filter(author=1)
    queryset = Post.objects.filter(status=1)
    template_name = "post_list.html"