from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Тільки поле для тексту коментаря
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Напишіть свій коментар тут...',
                'rows': 3,
            }),
        }
        labels = {
            'content': '',
        }