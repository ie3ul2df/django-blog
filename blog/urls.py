from django.urls import path
from . import views

urlpatterns = [
    # path('', views.hello_blog, name='hello_blog'),
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
