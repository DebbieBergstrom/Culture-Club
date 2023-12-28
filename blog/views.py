from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import Blogpost, UserProfile
from .forms import CommentForm, UserProfileForm, BlogpostForm


class BlogpostCreateView(LoginRequiredMixin, generic.CreateView):
    # A view for creating a new blog post
    model = Blogpost
    form_class = BlogpostForm
    template_name = 'blogpost_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('blogpost_detail', kwargs={'slug': self.object.slug})


class BlogpostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Blogpost
    form_class = BlogpostForm
    template_name = 'blogpost_update.html'
    success_url = reverse_lazy('blogpost_detail')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blogpost_detail', kwargs={'slug': self.object.slug})


class BlogpostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Blogpost
    template_name = 'blogpost_confirm_delete.html'
    success_url = reverse_lazy('home') #later change redirect to the users list of its own blogposts


class BlogPostList(generic.ListView):
    """
    A view that displays a list of blog posts. It inherits from Django's generic ListView.
    The view filters blog posts by their status and orders them by the creation date.
    Pagination is applied to limit the number of posts displayed per page.
    """
    model = Blogpost
    queryset = Blogpost.objects.filter(status=1).order_by('-created_on')
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
    """
    A view for displaying the detail of a specific blog post, identified by its slug.
    It handles both GET requests to display the post and its comments, and POST requests
    for submitting comments on the post.
    """
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
    """
    A view for handling the liking and unliking of a blog post.
    It updates the like status of a post for the logged-in user.
    """
    def post(self, request, slug, *args, **kwargs):
        blogpost = get_object_or_404(Blogpost, slug=slug)
        if blogpost.likes.filter(id=request.user.id).exists():
            blogpost.likes.remove(request.user)
        else:
            blogpost.likes.add(request.user)

        return HttpResponseRedirect(reverse('blogpost_detail', args=[slug]))


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    """
    A view for displaying the profile of the currently logged-in user.
    It fetches and displays the user's profile data.
    """
    def get(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        context = {
            'profile': user_profile,
            'is_own_profile': True
        }
        return render(request, 'profile.html', context)
        

class OtherUserProfileView(View):
    """
    A view for displaying the profile of another user, specified by their username.
    It retrieves and displays the profile information of the specified user.
    """
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        user_profile = get_object_or_404(UserProfile, user=user)
        context = {
            'profile': user_profile,
            'is_own_profile': request.user == user
        }
        return render(request, 'profile.html', context)


class ProfileEditView(LoginRequiredMixin, View):
    """
    A view for editing the profile of the currently logged-in user.
    It handles GET requests to display the profile edit form and POST requests
    to submit the form and update the user's profile.
    """
    def get(self, request):
        form = UserProfileForm(instance=request.user.userprofile)
        return render(request, 'profile_edit.html', {'form': form})

    def post(self, request):
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, 'profile_edit.html', {'form': form})
