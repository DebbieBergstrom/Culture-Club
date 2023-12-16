from django.shortcuts import render
from django.views import generic
from .models import Blogpost, Comment, MediaCategory


class BlogPostList(generic.ListView):
    model = Blogpost
    queryset = Blogpost.objects.filter(status=1).order_by('created_on')
    context_object_name = 'blogposts'
    template_name = 'index.html'
    paginate_by = 6