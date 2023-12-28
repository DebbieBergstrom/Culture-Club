from . import views
from django.urls import path

urlpatterns = [
    # Home page showing a list of blog posts
    path("", views.BlogPostList.as_view(), name="home"),

    # User's own profile page
    path('profile/', views.ProfileView.as_view(), name='profile'),

    # Profile page of other users, accessible via their username
    path('user/<str:username>/', views.OtherUserProfileView.as_view(), name='other_user_profile'),

    # Page for editing the currently logged-in user's profile
    path('profile/edit/', views.ProfileEditView.as_view(), name='profile_edit'),

    # Detail page for a specific blog post, identified by its slug
    path('<slug:slug>/', views.BlogPostDetail.as_view(), name='blogpost_detail'),

    # Endpoint for liking or unliking a blog post
    path('like/<slug:slug>/', views.LikeUnlike.as_view(), name='like_unlike'),
]