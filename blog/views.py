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

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
        },
    )


#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------------------------------------------------

# 👉 https://www.youtube.com/watch?v=h05UEays2KI
# 👉 render(request, template, context)


# 🔹 1. request

#         This is the incoming HTTP request (from the browser).
#         It tells Django whos asking for the page and how (GET or POST).
#         Required to manage sessions, authentication, etc.


# 🔹 2. "blog/post_detail.html"

#         This is the template file that Django will use to build the HTML.
#         It contains placeholders like {{ post.title }} and {{ post.content }}.
#         It gets filled with real data (from the third argument).


# 🔹 3. {"post": post}

#         This is the context dictionary.
#         It passes your dynamic data (like the post) from the view to the template.
#         You use this data in the template like {{ post.title }}.



# 🔍 So what data is being passed?
#     The post object contains all the fields from your Post model. That usually includes:

#     title	    ➜      {{ post.title }}	The blog post title
#     slug	    ➜      Not shown, but used in the URL	e.g., my-first-post
#     content	    ➜      `{{ post.content	safe }}`
#     author	    ➜      {{ post.author }}	Who wrote the post
#     created_on	➜      {{ post.created_on }}	When the post was published
#     excerpt     ➜      (optional)	{{ post.excerpt }}	A short preview of the post
#     status	    ➜      Used in filter, not shown directly	Published/Draft status


# 🔍 So what data is being passed with request?
#     The request object holds everything the browser sends to Django when a user visits a page or submits something. That includes:

#     request.method  ➜ Not shown in template	HTTP method used (e.g., "GET", "POST")	
#     request.user    ➜ Used in views (request.user)	The current user (Anonymous or logged-in user)	
#     request.GET     ➜ Used in views (request.GET.get("q"))	Query parameters from the URL like ?q=search-term	
#     request.POST    ➜ Used in views (request.POST.get("name"))	Form data submitted via POST method	
#     request.COOKIES ➜ Used in views (request.COOKIES['sessionid'])	Cookies sent by the browser	
#     request.session ➜ Used in views (request.session['key'])	User session data (shopping cart, login info, etc.)	
#     request.headers ➜ Used in views (request.headers['User-Agent'])	HTTP headers, like browser type or language	

#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------------------------------------------------