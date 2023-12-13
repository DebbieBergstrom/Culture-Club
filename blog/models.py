from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))


class Blogpost(models.Model):
    """
    The Blogpost model represents a blog post in the Culture Club application. 
    It contains information about the blog title, slug, author, created and updated timestamps, 
    the content of the post, an excerpt, the post status (draft or published), 
    an image for the post, the category of media it pertains to, and the year of release 
    if applicable. Users can also like or bookmark posts, which is represented by 
    many-to-many relationships with the User model.
    """
    blog_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    featured_image = CloudinaryField('image', default='placeholder')
    media_category = models.ForeignKey('MediaCategory', on_delete=models.CASCADE, related_name='blog_posts')
    release_year = models.IntegerField()
    media_link = models.URLField()
    likes = models.ManyToManyField(User, related_name='blogpost_likes', blank=True)
    bookmarks = models.ManyToManyField(User, related_name='blogpost_bookmarks', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.blog_title

    def number_of_likes(self):
        return self.likes.count()

    def number_of_bookmarks(self):
        return self.bookmarks.count()


class Comment(models.Model):
    """
    The Comment model represents a comment made on a blog post.
    It stores the content of the comment, the creation date and time, and a boolean flag to indicate 
    whether the comment has been approved by the site administrators. Each comment is linked to a specific 
    blog post and user who authored the comment.
    """
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    post = models.ForeignKey('Blogpost', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment {self.body} by {self.user.username}"