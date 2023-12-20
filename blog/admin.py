from django.contrib import admin
from .models import Blogpost, Comment, MediaCategory
from django_summernote.admin import SummernoteModelAdmin


@admin.register(MediaCategory)
class MediaCategoryAdmin(admin.ModelAdmin):
    list_display = ('media_name',)
    search_fields = ('media_name',)


@admin.register(Blogpost)
class PostAdmin(SummernoteModelAdmin):
    
    list_display = ('blog_title', 'slug', 'status', 'created_on')
    search_fields = ('blog_title', 'content')
    prepopulated_fields = {'slug': ('blog_title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('user', 'body', 'blogpost', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('user', 'body', 'blogpost')
    actions = ['approved_comments']
    
    def approved_comments(self, request, queryset):
        queryset.update(approved=True)
