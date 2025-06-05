## 🧭 Django View Flow – How Everything Connects

When a user visits your website (e.g., `http://example.com/`), Django follows this step-by-step flow to process the request and return a response.

### 🔄 Flow Overview

```
🔽 User visits your homepage: http://example.com/

1️⃣ codestar/urls.py  (Project URLs)
┌────────────────────────────────────────────┐
│ from django.urls import path, include      │
│ urlpatterns = [                            │
│   path("", include("blog.urls"))           │
│ ]                                          │
└────────────────────────────────────────────┘
             🔽
2️⃣ blog/urls.py  (App URLs)
┌────────────────────────────────────────────┐
│ from django.urls import path               │
│ from . import views                        │
│ urlpatterns = [                            │
│   path("", views.PostList.as_view())       │
│ ]                                          │
└────────────────────────────────────────────┘
             🔽
3️⃣ blog/views.py  (View Logic)
┌────────────────────────────────────────────┐
│ from django.views import generic           │
│ from .models import Post                   │
│                                            │
│ class PostList(generic.ListView):          │
│     queryset = Post.objects.all()          │
│     template_name = "blog/post_list.html"  │
└────────────────────────────────────────────┘
             🔽
4️⃣ blog/models.py  (Data Model)
┌────────────────────────────────────────────┐
│ from django.db import models               │
│                                            │
│ class Post(models.Model):                  │
│     title = models.CharField(...)          │
│     content = models.TextField()           │
└────────────────────────────────────────────┘
             🔽
5️⃣ blog/templates/blog/post_list.html  (HTML View)
┌────────────────────────────────────────────┐
│ {% for post in posts %}                    │
│   <h2>{{ post.title }}</h2>                │
│ {% endfor %}                               │
└────────────────────────────────────────────┘

🎉 Final result: User sees a list of blog posts in their browser!

```
