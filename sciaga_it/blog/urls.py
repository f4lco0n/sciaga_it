from django.urls import path, include
from . import views
from .views import HomeView, PostDetailView, PostCreateView
urlpatterns = [
    # path('', views.home, name='home'),
    path('',HomeView.as_view(), name='home'),
    path('post_details/<int:pk>', PostDetailView.as_view(), name='post-details' ),
    path('add_post/', PostCreateView.as_view(), name='add_post'),

]
