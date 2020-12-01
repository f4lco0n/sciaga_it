from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, UpdatePostForm
from django.urls import reverse_lazy


# Create your views here.


class HomeView(ListView):
    model = Post
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        result = Post.objects.filter(is_private=0).count()
        return render(request, self.template_name, {'result': result})


class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    ordering = ['-publication_date']

    def get(self, request, *args, **kwargs):
        result = Post.objects.filter(is_private=0)
        return render(request, self.template_name, {'result': result})


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


class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')


def category_view(request, cat):
    category = Category.objects.get(name=cat.replace('-', ' '))
    category_posts = Post.objects.filter(category_id=category.id, is_private=0)
    return render(request, 'post_list.html', {'result': category_posts,
                                              'list_title': 'Ściągi z kategorii: {0}'.format(category.name)})


def show_user_post_view(request, username):
    user = User.objects.get(username=username)
    result = Post.objects.filter(author_id=user.id, is_private=0)
    return render(request, 'post_list.html', {'result': result,
                                              'list_title': 'Ściągi użytkownika: {0}'.format(user.username)})
