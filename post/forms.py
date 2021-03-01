from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = [
            'text_description',
            'content',
            'post_type',
            'shared_with',
        ]

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = [
            'comment_text'
        ]


