from django.urls import path, include
from . import views
from .views import HomeView, PostDetailView, PostCreateView, UpdatePostView, DeletePostView, \
    category_view, PostListView, show_user_profile_view, TutorialListView, \
    TutorialDetailView, TutorialCreateView, TutorialUpdateView, DeleteTutorialView, SearchResultsView

urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('post_details/<int:pk>', PostDetailView.as_view(), name='post-details'),
    path('post_list/', PostListView.as_view(), name='post_list'),
    path('add_post/', PostCreateView.as_view(), name='add_post'),
    path('post_details/edit/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('post_details/<int:pk>/delete', DeletePostView.as_view(), name='delete-post'),
    path('category/<str:cat>/', category_view, name='category'),
    path('profile/<str:username>/', show_user_profile_view, name='user_profile'),

    # TUTORIALS
    path('tutorial_list/', TutorialListView.as_view(), name='tutorial_list'),
    path('tutorial_details/<int:pk>', TutorialDetailView.as_view(), name='tutorial-details'),
    path('add_tutorial/', TutorialCreateView.as_view(), name='add_tutorial'),
    path('tutorial_details/edit/<int:pk>', TutorialUpdateView.as_view(), name='update-tutorial'),
    path('tutorial_details/<int:pk>/delete', DeleteTutorialView.as_view(), name='delete-tutorial'),

    # SEARCH
    path('search/', SearchResultsView.as_view(), name='search_results')
]
