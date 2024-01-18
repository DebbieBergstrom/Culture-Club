from django.urls import path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
     path("", views.BlogPostList.as_view(), name="home"),
     path('blogpost/create/', views.BlogpostCreateView.as_view(),
          name='blogpost_create'),
     path('blogpost/<slug:slug>/', views.BlogPostDetail.as_view(),
          name='blogpost_detail'),
     path('blogpost/update/<slug:slug>/', views.BlogpostUpdateView.as_view(),
          name='blogpost_update'),
     path('blogpost/delete/<slug:slug>/', views.BlogpostDeleteView.as_view(),
          name='blogpost_delete'),
     path('my-posts/', views.MyBlogPostsView.as_view(), name='my_posts'),
     path('blogpost/like/<slug:slug>/', views.LikeUnlike.as_view(),
          name='like_unlike'),
     path('profile/', views.ProfileView.as_view(), name='profile'),
     path('user/<str:username>/', views.OtherUserProfileView.as_view(),
          name='other_user_profile'),
     path('profile/edit/', views.ProfileEditView.as_view(),
          name='profile_edit'),
     path('about-us/', TemplateView.as_view(template_name='about_us.html'),
          name='about_us'),
     path('saved-for-later/', views.bookmarked, name='bookmarked'),
     path('bookmark-unbookmark/<slug:slug>/',
          views.BookmarkUnbookmark.as_view(), name='bookmark_unbookmark'),
]
