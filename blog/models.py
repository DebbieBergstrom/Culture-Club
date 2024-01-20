from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

current_year = timezone.now().year


def validate_year(value):
    """
    Validates that a given year (value) is within the range of year 1800 and
    the current year. This function ensures that the 'release year' input
    falls within a reasonable and valid range. If the input year is outside
    this range, a ValidationError is raised.
    """
    current_year = timezone.now().year
    if not (1800 <= value <= current_year):
        raise ValidationError(
            _("Please enter a year between 1800 and %(current_year)s"),
            params={'current_year': current_year},
        )


STATUS = ((0, 'Draft'), (1, 'Published'))


class MediaCategory(models.Model):
    """
    MediaCategory model stores various categories for cultural media,
    such as movies, books, music, and podcasts. Each entry in this model
    represents a distinct category of media, which can be used to classify
    blog posts in the Culture Club application. The 'media_name' field
    is unique to ensure each category is only represented once.
    """
    media_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.media_name

    class Meta:
        verbose_name_plural = "Media Categories"


class UserProfile(models.Model):
    """
    A UserProfile model extends the built-in User model to include
    additional user information. It is linked to the User model with a
    OneToOneField, meaning each user will only have one profile. This model
    includes fields for a profile image, bio, country, and personal top
    picks in various media categories if the user wants to.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = CloudinaryField('image', default='placeholder')
    bio = models.TextField(max_length=350, blank=True)
    country = models.CharField(max_length=70, blank=True)
    top_movies = models.CharField(max_length=255, blank=True)
    top_series = models.CharField(max_length=255, blank=True)
    top_music_albums = models.CharField(max_length=255, blank=True)
    top_books = models.CharField(max_length=255, blank=True)
    top_podcasts = models.CharField(max_length=255, blank=True)
    top_miscellaneous = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username


class Blogpost(models.Model):
    """
    Represents a blog post in the Culture Club application. It includes details
    like the title, slug, author, timestamps, content, excerpt, status,
    featured image, media category, and the year of release. It also supports
    likes and bookmarks through many-to-many relationships with the User model.
    """

    # Title of the blog post; must be unique
    blog_title = models.CharField(max_length=200, unique=True)

    # URL-friendly slug for the blog post; generated automatically from the
    # title and must be unique
    slug = models.SlugField(max_length=200, unique=True)

    # Reference to the User model; indicates the author of the blog post
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts'
    )
    # Timestamps for when the post was created and last updated
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    # Main content of the blog post
    content = models.TextField(max_length=10000)

    # Short excerpt or summary of the blog post; optional
    excerpt = models.TextField(max_length=70, blank=True)

    # Indicates the current status of the blog post (e.g., draft, published)
    status = models.IntegerField(choices=STATUS, default=1)

    # CloudinaryField for storing images, with a default placeholder image
    featured_image = CloudinaryField('image', default='blogpost_placeholder')

    # Reference to a MediaCategory instance; categorizes the blog post
    media_category = models.ForeignKey(
        'MediaCategory', on_delete=models.SET_NULL,
        related_name='blog_posts', null=True, blank=False
    )
    # Year of release for the media being discussed; validated by validate_year
    release_year = models.IntegerField(validators=[validate_year])

    # Optional URL field for linking to external media or references
    media_link = models.URLField()

    # Many-to-many relationships for likes and bookmarks; users can like or
    # bookmark the post
    likes = models.ManyToManyField(
        User, related_name='blogpost_likes', blank=True
    )
    bookmarks = models.ManyToManyField(
        User, related_name='blogpost_bookmarks', blank=True
    )

    def save(self, *args, **kwargs):
        # Automatically generate a slug from the blog title if not provided
        if not self.slug:
            self.slug = slugify(self.blog_title)

        # Set default image only if none is provided
        if not self.featured_image:
            self.featured_image = 'blogpost_placeholder'

        super(Blogpost, self).save(*args, **kwargs)

    def number_of_likes(self):
        # Return the count of likes for the blog post
        return self.likes.count()

    def number_of_bookmarks(self):
        # Return the count of bookmarks for the blog post
        return self.bookmarks.count()


class Comment(models.Model):
    """
    The Comment model represents a comment made on a blog post.
    It stores the content of the comment, the creation date and time, and a
    boolean flag to indicate whether the comment has been approved by the site
    administrators. Each comment is linked to a specific blog post and user who
    authored the comment.
    """
    body = models.TextField(max_length=1000)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    blogpost = models.ForeignKey('Blogpost', on_delete=models.CASCADE,
                                 related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} by {self.user.username}"
