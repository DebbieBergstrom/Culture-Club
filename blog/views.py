from django.views import generic
from .models import Blogpost, Comment, MediaCategory


class PostList(generic.ListView):
    model = Blogpost
    queryset = Blogpost.objects.filter(status=1).order_by('created_on')
    template_name = 'index.html'
    paginate_by = 6