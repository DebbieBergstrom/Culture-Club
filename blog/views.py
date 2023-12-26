from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Blogpost, UserProfile
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import CommentForm


class BlogPostList(generic.ListView):
    model = Blogpost
    queryset = Blogpost.objects.filter(status=1).order_by('created_on')
    context_object_name = 'blogposts'
    template_name = 'index.html'
    paginate_by = 6
    
    def dispatch(self, request, *args, **kwargs):
        """
    Override the dispatch method to check user authentication status.
    This method is called before any other method in the view. It checks if the user
    is authenticated. If the user is not authenticated, they are redirected to the login
    page. Otherwise, the normal flow of the ListView is executed.
    """
        if not request.user.is_authenticated:
            return redirect('account_login')
        return super().dispatch(request, *args, **kwargs)


class BlogPostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Blogpost.objects.filter(status=1)
        blogpost = get_object_or_404(queryset, slug=slug)
        comments = blogpost.comments.filter(approved=False).order_by("created_on")
        liked = False
        if blogpost.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blogpost_detail.html",
            {
                "blogpost": blogpost,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
    
    def post(self, request, slug, *args, **kwargs):
        queryset = Blogpost.objects.filter(status=1)
        blogpost = get_object_or_404(queryset, slug=slug)
        comments = blogpost.comments.filter(approved=False).order_by("created_on")
        liked = blogpost.likes.filter(id=request.user.id).exists()

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.blogpost = blogpost
            comment.user = request.user
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "blogpost_detail.html",
            {
                "blogpost": blogpost,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": comment_form
            },
        )


class LikeUnlike(View):
    def post(self, request, slug, *args, **kwargs):
        blogpost = get_object_or_404(Blogpost, slug=slug)
        if blogpost.likes.filter(id=request.user.id).exists():
            blogpost.likes.remove(request.user)
        else:
            blogpost.likes.add(request.user)

        return HttpResponseRedirect(reverse('blogpost_detail', args=[slug]))


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        context = {
            'profile': user_profile
        }
        return render(request, 'profile.html', context)
        

class OtherUserProfileView(View):
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        user_profile = get_object_or_404(UserProfile, user=user)
        context = {
            'profile': user_profile,
            'is_own_profile': request.user == user
        }
        return render(request, 'profile.html', context)
