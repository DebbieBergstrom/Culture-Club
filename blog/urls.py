from . import views
from django.urls import path

urlpatterns = [
    path("", views.BlogPostList.as_view(), name="home"),
    path('<slug:slug>/', views.BlogPostDetail.as_view(), name='blogpost_detail'),
    path('like/<slug:slug>/', views.LikeUnlike.as_view(), name='like_unlike'),
]