from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import UserProfile, MediaCategory, Blogpost, Comment


class TestModels(TestCase):
    """
    Test cases for models in the Culture Club app
    """

    def setUp(self):
        # Create a test user.
        # The signal will automatically create a UserProfile
        self.test_user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

        # Create a test media category
        self.test_category = MediaCategory.objects.create(
            media_name="Test Category"
        )

        # Create a test blog post
        self.test_blogpost = Blogpost.objects.create(
            blog_title="Test Title",
            content="Test Content",
            author=self.test_user,
            media_category=self.test_category,
            release_year=2021
        )

        # Create a test comment
        self.test_comment = Comment.objects.create(
            body="Test Comment Body",
            blogpost=self.test_blogpost,
            user=self.test_user,
            approved=True
        )

    def test_user_profile_creation(self):
        """
        Test if a user profile is automatically created when
        a new user is created.
        """
        self.assertTrue(
            UserProfile.objects.filter(user=self.test_user).exists()
        )

    def test_media_category_creation(self):
        """
        Test if a media category is created successfully.
        """
        self.assertEqual(self.test_category.media_name, "Test Category")

    def test_blogpost_creation(self):
        """
        Test if a blog post is created successfully.
        """
        self.assertEqual(self.test_blogpost.blog_title, "Test Title")
        self.assertEqual(self.test_blogpost.author, self.test_user)
        self.assertEqual(
            self.test_blogpost.media_category, self.test_category
        )

    def test_comment_creation(self):
        """
        Test if a comment is created successfully and linked
        to a blog post and a user.
        """
        self.assertEqual(self.test_comment.body, "Test Comment Body")
        self.assertEqual(self.test_comment.blogpost, self.test_blogpost)
        self.assertEqual(self.test_comment.user, self.test_user)
        self.assertTrue(self.test_comment.approved)
