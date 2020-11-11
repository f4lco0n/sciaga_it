from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = "home.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "post_details.html"

class PostCreateView(CreateView):
    model = Post
    template_name = "add_post.html"
    fields = '__all__'