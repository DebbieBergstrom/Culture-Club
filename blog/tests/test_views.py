from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Blogpost, MediaCategory, Comment


class TestViews(TestCase):
    
    def setUp(self):
        """
        Set up initial data for testing: creating users, blogposts,
        and amedia category.
        """
        self.client = Client()

        # Create two users - one for testing ownership,
        # another for unauthorized access
        self.owner_user = User.objects.create_user(
            username='owneruser', password='123password'
        )
        self.other_user = User.objects.create_user(
            username='otheruser', password='123password'
        )

        self.category = MediaCategory.objects.create(media_name="Test Category")

        self.owner_blogpost = Blogpost.objects.create(
            blog_title="Owner's Post",
            content="Test Content",
            author=self.owner_user,
            media_category=self.category,
            release_year=2021,
            status=1
        )

        self.other_blogpost = Blogpost.objects.create(
            blog_title="Other's Post",
            content="Test Content",
            author=self.other_user,
            media_category=self.category,
            release_year=2021,
            status=1
        )

        self.comment = Comment.objects.create(
            body="Test Comment",
            blogpost=self.owner_blogpost,
            user=self.owner_user,
            approved=True
        )

        # Logging in with the owner user for tests that require an authenticated user
        self.client.login(username='owneruser', password='123password')


# BLOGPOST RELATED TESTS
    def test_BlogPostList_GET(self):
        """
        Test BlogPostList view for successful response and correct template.
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertIn('blogposts', response.context)


    def test_BlogpostCreateView_GET(self):
        """
        Test BlogpostCreateView for successful GET by an authenticated user.
        """
        self.client.login(username='owneruser', password='123password')
        response = self.client.get(reverse('blogpost_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogpost_create.html')


    def test_BlogpostUpdateView_GET(self):
        """
        Test BlogpostUpdateView to load correctly for the post's owner.
        """
        self.client.login(username='owneruser', password='123password')
        response = self.client.get(reverse('blogpost_update', args=[self.owner_blogpost.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogpost_update.html')


    def test_BlogpostDeleteView_GET(self):
        """
        Test BlogpostDeleteView to load correctly for the post's owner.
        """
        self.client.login(username='owneruser', password='123password')
        response = self.client.get(reverse('blogpost_delete', args=[self.owner_blogpost.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogpost_delete.html')


    def test_MyBlogPostsView_GET(self):
        """
        Test MyBlogPostsView to display logged-in user's posts.
        """
        self.client.login(username='owneruser', password='123password')
        response = self.client.get(reverse('my_posts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_posts.html')


    def test_MyBlogPostsView_access(self):
        """
        Test access to MyBlogPostsView by a different user.
        """
        self.client.login(username='otheruser', password='123password')
        response = self.client.get(reverse('my_posts'))
        self.assertEqual(response.status_code, 200)


    def test_BlogPostDetail_GET(self):
        """
        Test BlogPostDetail view for correct blog post details display.
        """
        response = self.client.get(reverse('blogpost_detail', args=[self.owner_blogpost.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogpost_detail.html')


    def test_LikeUnlike_POST(self):
        """
        Test LikeUnlike view to handle POST requests for liking/unliking.
        """
        self.client.login(username='owneruser',
        password='123password')
        response = self.client.post(reverse('like_unlike', args=[self.owner_blogpost.slug]))
        self.assertEqual(response.status_code, 302)


    def test_bookmarked_GET(self):
        """
        Test bookmarked view to display logged-in user's bookmarked posts.
        """
        self.client.login(username='owneruser', password='123password')
        response = self.client.get(reverse('bookmarked'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookmarked.html')


    def test_BookmarkUnbookmark_POST(self):
        """
        Test BookmarkUnbookmark view for POST requests to bookmark/unbookmark.
        """
        self.client.login(username='owneruser', password='123password')
        response = self.client.post(reverse('bookmark_unbookmark', args=[self.owner_blogpost.slug]))
        self.assertEqual(response.status_code, 302)


# PROFILE RELATED TESTS
    def test_ProfileView_GET(self):
        """
        Test ProfileView for successful response and correct template.
        """
        self.client.login(username='owneruser', password='123password')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
        self.assertIn('profile', response.context)


    def test_OtherUserProfileView_GET(self):
        """
        Test OtherUserProfileView for successful response and correct template.
        """
        self.client.login(username='owneruser', password='123password')
        response = self.client.get(reverse('other_user_profile', args=[self.other_user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')


    def test_ProfileEditView_GET(self):
        """
        Test ProfileEditView for successful GET by the profile owner.
        """
        self.client.login(username='owneruser', password='123password')
        response = self.client.get(reverse('profile_edit'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile_edit.html')


    def test_ProfileEditView_access(self):
        """
        Test access to ProfileEditView by a different user.
        """
        self.client.login(username='otheruser', password='123password')
        response = self.client.get(reverse('profile_edit'))
        self.assertEqual(response.status_code, 200)


    def test_ProfileDeleteView_GET(self):
        """
        Test ProfileDeleteView for successful GET by the profile owner.
        """
        self.client.login(username='owneruser', password='123password')
        response = self.client.get(reverse('account_delete', args=[self.owner_user.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account_manage.html')


    def test_ProfileDeleteView_access(self):
        """
        Test access to ProfileDeleteView by a different user.
        """
        self.client.login(username='otheruser', password='123password')
        response = self.client.get(reverse('account_delete', args=[self.other_user.pk]))
        self.assertEqual(response.status_code, 200)


# ERROR HANDLER RELATED TESTS

    def test_BlogpostUpdateView_unauthorized_access(self):
        """
        Test unauthorized access to BlogpostUpdateView.
        """
        self.client.login(username='otheruser', password='123password')
        response = self.client.get(reverse('blogpost_update', args=[self.owner_blogpost.slug]))
        self.assertEqual(response.status_code, 404)
        

    def test_BlogpostDeleteView_unauthorized_access(self):
        """
        Test unauthorized access to BlogpostDeleteView.
        """
        self.client.login(username='otheruser', password='123password')
        response = self.client.get(reverse('blogpost_delete', args=[self.owner_blogpost.slug]))
        self.assertEqual(response.status_code, 404)


    def test_BlogPostList_method_not_allowed(self):
        """
        Test making a POST request to a view that only allows GET.
        """
        response = self.client.post(reverse('home'))
        self.assertEqual(response.status_code, 405)
