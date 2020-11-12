from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, UpdatePostForm
from django.urls import reverse_lazy
# Create your views here.


class HomeView(ListView):
    model = Post
    template_name = "home.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "post_details.html"

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    # fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = "update_post.html"
    # fields = ('title', 'title_tag','body')

class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')