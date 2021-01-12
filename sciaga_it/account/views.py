from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from blog.models import Profile
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, EditProfilePageForm


class UserRegisterView(generic.CreateView):
    """view which allows create user's account and profile"""
    form_class = SignUpForm
    template_name = 'registration/register.html'

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)
        return super(UserRegisterView, self).form_valid(form)

    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    """view which allows users to edit their personal data (first name, last name, email"""
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'

    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('user_profile', args=(self.request.user.username,))


class ProfileEditView(generic.UpdateView):
    """view which allows users to edit fields like social media, bio, profile picture"""
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    form_class = EditProfilePageForm
    success_url = reverse_lazy('user_profile')

    def get_success_url(self):
        return reverse_lazy('user_profile', args=(self.request.user.username,))


class ChangePasswordView(PasswordChangeView):
    """view which allows user to change their password"""
    form_class = PasswordChangingForm
    success_url = reverse_lazy('home')
