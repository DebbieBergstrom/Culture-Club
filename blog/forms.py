from django import forms
from .models import Comment, UserProfile, Blogpost
import datetime


class BlogpostForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = ['blog_title', 'content', 'excerpt', 'status', 'featured_image', 'media_category', 'release_year', 'media_link']
        
        widgets = {
            'blog_title': forms.TextInput(attrs={'placeholder': 'Enter the title of the blog post...'}),
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your blog content here (max length 2000 characters)...', 'maxlength': '2000'}),
            'excerpt': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Write a short excerpt...(max length 100 characters)', 'maxlength': '100'}),
            'release_year': forms.NumberInput(attrs={'min': 1800, 'max': datetime.datetime.now().year, 'placeholder': 'YYYY'}),
            'media_link': forms.URLInput(attrs={'placeholder': 'http://www.example.com'}),
        }

        labels = {
            'blog_title': '',
            'content': '',
            'excerpt': '',
            'release_year': '',
            'media_link': '',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'rows': 2, 'cols': 50, 'placeholder': 'Write your comment here...', 'max_length': '1000'}),
        }
        labels = {
            'body': '',
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image', 'bio', 'country', 'top_movies', 'top_series', 'top_music_albums', 'top_books', 'top_podcasts', 'top_miscellaneous']
