from django import forms
from .models import Post, Tutorial


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        bool_choices = ((True, 'Tak'), (False, 'Nie'))
        fields = ('title', 'title_tag','category',
                  'author','is_private','short_description', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control','value':'',
                                             'id': 'author_input','type': 'hidden'}),
            'is_private': forms.Select(choices=bool_choices, attrs={'class': 'form-control'}),
            'short_description': forms.Textarea(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }

        labels = {
            "title": "Tytuł ściągi",
            "title_tag": "Tag ściągi",
            "category": "Kategoria",
            "author": "Autor",
            "is_private": "Post prywatny",
            "short_description": "Opis krótki",
            "body": "Zawartość"
        }

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        bool_choices = ((True, 'Tak'), (False, 'Nie'))
        fields = ('title', 'title_tag','category',
                  'is_private','short_description','body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'is_private': forms.Select(choices=bool_choices, attrs={'class': 'form-control'}),
            'short_description': forms.Textarea(attrs={'class': 'form-control',
                                                       'placeholder': 'Kliknij link powyżej aby zobaczyć post'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

        labels = {
            "title": "Tytuł ściągi",
            "title_tag": "Tag ściągi",
            "category": "Kategoria",
            "is_private": "Post prywatny",
            "short_description": "Opis krótki",
            "body": "Zawartość"
        }


class TutorialForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields = ('tutorial_title', 'tutorial_title_tag','tutorial_category',
                  'tutorial_author','tutorial_short_description', 'tutorial_body')

        widgets = {
            'tutorial_title': forms.TextInput(attrs={'class': 'form-control'}),
            'tutorial_title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'tutorial_category': forms.Select(attrs={'class': 'form-control'}),
            'tutorial_author': forms.TextInput(attrs={'class': 'form-control','value':'',
                                             'id': 'author_input','type': 'hidden'}),
            'tutorial_short_description': forms.Textarea(attrs={'class': 'form-control'}),
            'tutorial_body': forms.Textarea(attrs={'class': 'form-control'}),

        }

        labels = {
            "tutorial_title": "Tytuł poradnika",
            "tutorial_title_tag": "Tag poradnika",
            "tutorial_category": "Kategoria",
            "tutorial_author": "Autor",
            "tutorial_short_description": "Opis krótki",
            "tutorial_body": "Zawartość"
        }