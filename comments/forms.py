from django import forms
from django.contrib.auth.models import User
from .models import Comment

def comment_validate(value):
    if len(value) < 1:
        raise forms.ValidationError(
        'Отзыв слишком короткий',
        params={'value': value},
        )     

    elif len(value) > 511:
        raise forms.ValidationError(
            'Отзыв слишком длинный',
            params={'value': value},
        )  



class WriteCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text',]
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 10, 'type' : 'text',}),
        }
        error_messages = {
            'text': {
                'max_length': ("Отзыв слишком длинный"),
            },
        }
    
