from django.test import SimpleTestCase
from django.views.generic.base import TemplateView
from django.urls import reverse, resolve
from blog.views import (BlogPostList, BlogpostCreateView, BlogPostDetail, 
                        BlogpostUpdateView, BlogpostDeleteView, MyBlogPostsView,
                        LikeUnlike, ProfileView, OtherUserProfileView, 
                        ProfileEditView, BookmarkUnbookmark, bookmarked)

class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, BlogPostList)


    def test_blogpost_create_url_resolves(self):
        url = reverse('blogpost_create')
        self.assertEqual(resolve(url).func.view_class, BlogpostCreateView)


    def test_blogpost_detail_url_resolves(self):
        url = reverse('blogpost_detail', args=['some-slug'])
        self.assertEqual(resolve(url).func.view_class, BlogPostDetail)


    def test_blogpost_update_url_resolves(self):
        url = reverse('blogpost_update', args=['some-slug'])
        self.assertEqual(resolve(url).func.view_class, BlogpostUpdateView)


    def test_blogpost_delete_url_resolves(self):
        url = reverse('blogpost_delete', args=['some-slug'])
        self.assertEqual(resolve(url).func.view_class, BlogpostDeleteView)


    def test_my_blog_posts_url_resolves(self):
        url = reverse('my_posts')
        self.assertEqual(resolve(url).func.view_class, MyBlogPostsView)


    def test_like_unlike_url_resolves(self):
        url = reverse('like_unlike', args=['some-slug'])
        self.assertEqual(resolve(url).func.view_class, LikeUnlike)


    def test_profile_url_resolves(self):
        url = reverse('profile')
        self.assertEqual(resolve(url).func.view_class, ProfileView)


    def test_other_user_profile_url_resolves(self):
        url = reverse('other_user_profile', args=['some-username'])
        self.assertEqual(resolve(url).func.view_class, OtherUserProfileView)


    def test_profile_edit_url_resolves(self):
        url = reverse('profile_edit')
        self.assertEqual(resolve(url).func.view_class, ProfileEditView)


    def test_bookmark_unbookmark_url_resolves(self):
        url = reverse('bookmark_unbookmark', args=['some-slug'])
        self.assertEqual(resolve(url).func.view_class, BookmarkUnbookmark)


    def test_bookmarked_url_resolves(self):
        url = reverse('bookmarked')
        self.assertEqual(resolve(url).func, bookmarked)


    def test_about_us_url_resolves(self):
        url = reverse('about_us')
        self.assertTrue(resolve(url).func.view_class, TemplateView)
