from django.urls import path, include
from .views import UserRegisterView, UserEditView, ChangePasswordView, ProfileEditView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/',ChangePasswordView.as_view(template_name='registration/change-password.html')),
    path('<int:pk>/edit_profile_page/', ProfileEditView.as_view(), name='edit_profile_page' )
]
