from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from blog.models import Profile
from django import forms


class SignUpForm(UserCreationForm):


    class Meta:
        model = User
        fields = ('username','password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, required=False,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class EditProfilePageForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('profile_picture','bio', 'occupation',
                  'website_url', 'facebook_url', 'instagram_url', 'github_url', 'twitter_url')

        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'website_url': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
            'github_url': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            "profile_picture": "Zdjęcie profilowe",
            "bio": "O mnie:",
            "occupation": "Zawód:",
            "website_url": "Strona:",
            "facebook_url": "Facebook:",
            "instagram_url": "Instagram",
            "github_url": "Github",
            "twitter_url": "Twitter"
        }


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                     'type': 'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                      'type': 'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                      'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

        labels = {
            "old_password": "Stare hasło",
            "new_password1": "Nowe hasło",
            "new_password2": "Powtórz nowe hasło"
        }
