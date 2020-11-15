from django.urls import path, include
from . import views
from .views import HomeView, PostDetailView, PostCreateView, UpdatePostView, DeletePostView, CategoryView, PostListView

urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('post_details/<int:pk>', PostDetailView.as_view(), name='post-details'),
    path('post_list/', PostListView.as_view(), name='post_list'),
    path('add_post/', PostCreateView.as_view(), name='add_post'),
    path('post_details/edit/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('post_details/<int:pk>/delete', DeletePostView.as_view(), name='delete-post'),
    path('category/<int:category_id>', CategoryView, name='category')

]
