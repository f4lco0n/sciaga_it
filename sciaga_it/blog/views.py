from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Tutorial
from .forms import PostForm, UpdatePostForm, TutorialForm, UpdateTutorialForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator


class HomeView(ListView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        posts = Post.objects.filter(is_private=0).count()
        tutorials = Tutorial.objects.all().count()
        users = User.objects.all().count()
        return render(request, self.template_name, {'posts': posts, 'tutorials': tutorials, 'users': users})


class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    ordering = ['-publication_date']

    def get(self, request, *args, **kwargs):
        result = Post.objects.filter(is_private=0)
        paginator = Paginator(result, 3)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, self.template_name, {'page_obj': page_obj})


class PostDetailView(DetailView):
    model = Post
    template_name = "post_details.html"


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = "update_post.html"


class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')


def category_view(request, cat):
    """view which returns all posts from clicked category and are not private"""
    category = Category.objects.get(name=cat.replace('-', ' '))
    category_posts = Post.objects.filter(category_id=category.id, is_private=0)
    return render(request, 'post_list.html', {'result': category_posts,
                                              'list_title': 'Ściągi z kategorii: {0}'.format(category.name)})


# TODO: rethink a way to display user's posts
def show_user_post_view(request, username):
    """view which returns all posts from clicked user"""
    user = User.objects.get(username=username)
    result = Post.objects.filter(author_id=user.id, is_private=0)
    return render(request, 'post_list.html', {'result': result,
                                              'list_title': 'Ściągi użytkownika: {0}'.format(user.username)})


def show_user_profile_view(request, username):
    """view which returns user's profile with basic info and all public posts"""
    user_profile = User.objects.get(username=username)
    user_posts = Post.objects.filter(author=user_profile, is_private=0)
    return render(request, 'user_profile.html', {'user_profile': user_profile, 'user_posts': user_posts})


class TutorialListView(ListView):
    model = Tutorial
    template_name = "tutorial_list.html"
    ordering = ['-publication_date']

    def get(self, request, *args, **kwargs):
        result = Tutorial.objects.all()
        paginator = Paginator(result, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, self.template_name, {'page_obj': page_obj})


class TutorialDetailView(DetailView):
    model = Tutorial
    template_name = "tutorial_details.html"


class TutorialCreateView(CreateView):
    model = Tutorial
    form_class = TutorialForm
    template_name = "add_tutorial.html"


class TutorialUpdateView(UpdateView):
    model = Tutorial
    form_class = UpdateTutorialForm
    template_name = "update_tutorial.html"


class DeleteTutorialView(DeleteView):
    model = Tutorial
    template_name = "delete_tutorial.html"
    success_url = reverse_lazy('home')


class SearchResultsView(ListView):
    model = Post
    template_name = 'search_result.html'

    def get(self, request, *args, **kwargs): # new
        query = self.request.GET.get('q')
        posts_list = list(Post.objects.filter(title__contains=query))
        tutorials_list = list(Tutorial.objects.filter(tutorial_title__contains=query))
        # print(posts_list, tutorials_list)
        # paginator = Paginator(result, 3)
        #
        # page_number = request.GET.get('page')
        # page_obj = paginator.get_page(page_number)
        return render(request, self.template_name, {'page_obj_posts': posts_list, 'page_obj_tutorials': tutorials_list})