from django import forms
from .models import Blog


class RegisterModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body', 'owner']
        labels = {
            'title': '标题',
            'body': '内容',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'owner': forms.HiddenInput(),
        }
