from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        bool_choices = ((True, 'Tak'), (False, 'Nie'))
        fields = ('title', 'title_tag','category', 'author','is_private', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control','value':'',
                                             'id': 'author_input','type': 'hidden'}),
            'is_private': forms.Select(choices=bool_choices, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }

        labels = {
            "title": "Tytuł ściągi",
            "title_tag": "Tag ściągi",
            "category": "Kategoria",
            "author": "Autor",
            "is_private": "Post prywatny",
            "body": "Zawartość"
        }

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        bool_choices = ((True, 'Tak'), (False, 'Nie'))
        fields = ('title', 'title_tag','category','is_private','body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'is_private': forms.Select(choices=bool_choices, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

        labels = {
            "title": "Tytuł ściągi",
            "title_tag": "Tag ściągi",
            "category": "Kategoria",
            "is_private": "Post prywatny",
            "body": "Zawartość"
        }