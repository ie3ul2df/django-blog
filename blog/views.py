from django.shortcuts import render, get_object_or_404
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
    # template_name = "post_list.html"
    template_name = "blog/index.html"
    paginate_by = 6


# # single post detail view
# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = "blog/post_detail.html"  # Make sure this matches your template


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )