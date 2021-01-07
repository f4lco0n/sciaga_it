from django.shortcuts import render
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, EditProfilePageForm
from blog.models import Profile


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)
        return super(UserRegisterView, self).form_valid(form)
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'

    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class ProfileEditView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    form_class = EditProfilePageForm
    success_url = reverse_lazy('user_profile')

    def get_success_url(self):
        return reverse_lazy('user_profile', args=(self.request.user.username,))


class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('home')
