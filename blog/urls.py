from . import views
from django.urls import path

urlpatterns = [
    path("", views.BlogPostList.as_view(), name="home"),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('user/<str:username>/', views.OtherUserProfileView.as_view(), name='other_user_profile'),
    path('<slug:slug>/', views.BlogPostDetail.as_view(), name='blogpost_detail'),
    path('like/<slug:slug>/', views.LikeUnlike.as_view(), name='like_unlike'),
]