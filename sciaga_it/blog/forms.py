from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag','category', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control','value':'',
                                             'id': 'author_input','type': 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }

        labels = {
            "title": "Tytuł ściągi",
            "title_tag": "Tag ściągi",
            "category": "Kategoria",
            "author": "Autor",
            "body": "Zawartość"
        }

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag','category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

        labels = {
            "title": "Tytuł ściągi",
            "title_tag": "Tag ściągi",
            "category": "Kategoria",
            "body": "Zawartość"
        }