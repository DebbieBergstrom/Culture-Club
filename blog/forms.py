from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'rows': 2, 'cols': 50, 'placeholder': 'Write your comment here...', 'max_length': '1000'}),
        }