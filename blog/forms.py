from django import forms
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from .models import Comment, UserProfile, Blogpost
import datetime


class BlogpostForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = ['blog_title', 'content', 'excerpt', 'status', 'featured_image', 'media_category', 'release_year', 'media_link']
        
        widgets = {
            'blog_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a title for your post...(max length 50 characters)','maxlength': '50'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Write your blog content here (max length 2000 characters)...', 'maxlength': '2000'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Write a short excerpt...(max length 70 characters)', 'maxlength': '70'}),
            'release_year': forms.NumberInput(attrs={'class': 'form-control', 'min': 1800, 'max': datetime.datetime.now().year, 'placeholder': 'Format YYYY'}),
            'media_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'e.g http://www.imdb.com'}),
        }

        # def clean_media_link(self):
        #     media_link = self.cleaned_data.get('media_link', '')
        #     if media_link and not media_link.startswith(('http://', 'https://')):
        #         media_link = 'http://' + media_link
        #     # Validate URL
        #     validate = URLValidator()
        #     try:
        #         validate(media_link)
        #     except ValidationError as e:
        #         raise forms.ValidationError("Invalid URL")
        #     return media_link


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'cols': 50, 'placeholder': 'Write your comment here...', 'max_length': '1000'}),
        }
        labels = {
            'body': '',
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image', 'bio', 'country', 'top_movies', 'top_series', 'top_music_albums', 'top_books', 'top_podcasts', 'top_miscellaneous']
        
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Write something about yourself (max length 350 characters)...', 'maxlength': '350'}),
        }
