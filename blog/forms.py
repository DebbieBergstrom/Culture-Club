from .models import Comment, UserProfile
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'rows': 2, 'cols': 50, 'placeholder': 'Write your comment here...', 'max_length': '1000'}),
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image', 'bio', 'country', 'top_movies', 'top_series', 'top_music_albums', 'top_books', 'top_podcasts', 'top_miscellaneous']
