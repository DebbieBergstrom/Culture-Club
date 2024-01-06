from django.urls import path
from . import views

urlpatterns = [
    # Display list of blog posts
    path("", views.BlogPostList.as_view(), name="home"),
    
    # Create a new blog post
    path('blogpost/create/', views.BlogpostCreateView.as_view(), name='blogpost_create'),

    # Display detail of a specific blog post
    path('blogpost/<slug:slug>/', views.BlogPostDetail.as_view(), name='blogpost_detail'),

    # Update an existing blog post
    path('blogpost/update/<slug:slug>/', views.BlogpostUpdateView.as_view(), name='blogpost_update'),

    # Delete a blog post
    path('blogpost/delete/<slug:slug>/', views.BlogpostDeleteView.as_view(), name='blogpost_delete'),
    
    # Display list of the logged in users own posts
    path('my-posts/', views.MyBlogPostsView.as_view(), name='my_posts'),

    # Like or unlike a blog post
    path('blogpost/like/<slug:slug>/', views.LikeUnlike.as_view(), name='like_unlike'),

    # Display the profile of the current user
    path('profile/', views.ProfileView.as_view(), name='profile'),

    # Display the profile of another user
    path('user/<str:username>/', views.OtherUserProfileView.as_view(), name='other_user_profile'),

    # Edit the profile of the current user
    path('profile/edit/', views.ProfileEditView.as_view(), name='profile_edit'),
]