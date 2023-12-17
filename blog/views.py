from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Blogpost, Comment, MediaCategory


class BlogPostList(generic.ListView):
    model = Blogpost
    queryset = Blogpost.objects.filter(status=1).order_by('created_on')
    context_object_name = 'blogposts'
    template_name = 'index.html'
    paginate_by = 6


class BlogPostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Blogpost.objects.filter(status=1)
        blogpost = get_object_or_404(queryset, slug=slug)
        comments = blogpost.comments.filter(approved=True).order_by("created_on")
        liked = False
        if blogpost.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blogpost_detail.html",
            {
                "blogpost": blogpost,
                "comments": comments,
                "liked": liked
            },
        )