from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Comment)  # ✅ Registered using default model admin
# admin.site.register(Post)

@admin.register(Post)         # ✅ Registered using Summernote-enhanced class
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}  # Slug auto-fills from title
    summernote_fields = ('content',)            # Rich text for content