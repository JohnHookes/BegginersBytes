from django import forms  # Make sure this import statement is present

from .models import Comment 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_title', 'body', 'review')