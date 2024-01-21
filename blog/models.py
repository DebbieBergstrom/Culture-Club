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
    blog_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=10000)
    excerpt = models.TextField(max_length=70, blank=True)
    status = models.IntegerField(choices=STATUS, default=1)
    featured_image = CloudinaryField('image', default='blogpost_placeholder')
    media_category = models.ForeignKey(
        'MediaCategory', on_delete=models.SET_NULL,
        related_name='blog_posts', null=True, blank=False
    )
    release_year = models.IntegerField(validators=[validate_year])
    media_link = models.URLField()
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
        return self.likes.count()

    def number_of_bookmarks(self):
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
