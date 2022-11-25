from django import forms
from django.contrib.auth.models import User
from .models import Comment

class WriteCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text',]
        widgets = {
            'text': forms.Textarea(),
        }