from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .models import Post, Category, Tutorial
from .forms import PostForm, UpdatePostForm, TutorialForm, UpdateTutorialForm


class HomeView(ListView): # pylint: disable=too-many-ancestors
    """home view which returns basic stats"""
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        posts = Post.objects.filter(is_private=0).count()
        tutorials = Tutorial.objects.all().count()
        users = User.objects.all().count()
        return render(request, self.template_name, {'posts': posts,
                                                    'tutorials': tutorials,
                                                    'users': users})


class PostListView(ListView):
    """view which returns all non private posts"""
    model = Post
    template_name = "post_list.html"
    ordering = ['publication_date']

    def get(self, request, *args, **kwargs):
        result = Post.objects.filter(is_private=0)
        paginator = Paginator(result, 5)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, self.template_name, {'page_obj': page_obj})


class PostDetailView(DetailView):
    """view which returns details about clicked post"""
    model = Post
    template_name = "post_details.html"


class PostCreateView(CreateView):
    """view which allows users create a post"""
    model = Post
    form_class = PostForm
    template_name = "add_post.html"


class UpdatePostView(UpdateView):
    """view which allows author to edit post"""
    model = Post
    form_class = UpdatePostForm
    template_name = "update_post.html"


class DeletePostView(DeleteView):
    """view which allows author to remove clicked post"""
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')


def category_view(request, cat):
    """view which returns all posts from clicked category and are not private"""
    category = Category.objects.get(name=cat.replace('-', ' '))
    category_posts = Post.objects.filter(category_id=category.id, is_private=0)
    category_tutorials = Tutorial.objects.filter(tutorial_category_id=category.id,
                                                 tutorial_is_private=0)
    return render(request, 'search_result.html', {'page_obj_posts': category_posts,
                                                  'page_obj_tutorials': category_tutorials,
                                                  'list_title': 'Publikacje z kategorii: ',
                                                  'query': category})


def show_user_profile_view(request, username):
    """view which returns user's profile with basic info and all public posts and tutorials"""
    user_profile = User.objects.get(username=username)
    user_posts = Post.objects.filter(author=user_profile, is_private=0)
    user_tutorials = Tutorial.objects.filter(tutorial_author=user_profile, tutorial_is_private=0)
    private_posts = Post.objects.filter(author=user_profile, is_private=1)
    private_tutorials = Tutorial.objects.filter(tutorial_author=user_profile, tutorial_is_private=1)
    return render(request, 'user_profile.html', {'user_profile': user_profile,
                                                 'user_posts': user_posts,
                                                 'user_tutorials': user_tutorials,
                                                 'private_posts': private_posts,
                                                 'private_tutorials': private_tutorials})


class TutorialListView(ListView):
    """view which returns all non private tutorials"""
    model = Tutorial
    template_name = "tutorial_list.html"
    ordering = ['-publication_date']

    def get(self, request, *args, **kwargs):
        result = Tutorial.objects.filter(tutorial_is_private=0)
        paginator = Paginator(result, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, self.template_name, {'page_obj': page_obj})


class TutorialDetailView(DetailView):
    """view which returns details about clicked tutorial"""
    model = Tutorial
    template_name = "tutorial_details.html"


class TutorialCreateView(CreateView):
    """view which allows users create a tutorial"""
    model = Tutorial
    form_class = TutorialForm
    template_name = "add_tutorial.html"


class TutorialUpdateView(UpdateView):
    """view which allows author to edit tutorial"""
    model = Tutorial
    form_class = UpdateTutorialForm
    template_name = "update_tutorial.html"


class DeleteTutorialView(DeleteView):
    """view which allows author to remove clicked post"""

    model = Tutorial
    template_name = "delete_tutorial.html"
    success_url = reverse_lazy('home')


class SearchResultsView(ListView):
    """view which returns all non private posts and tutorials based on query in search"""
    model = Post
    template_name = 'search_result.html'

    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')

        if query and len(query) > 0:
            title = "Wyniki wyszukiwania dla: "
            posts_list = list(Post.objects.filter(
                title__contains=query,
                is_private=0))
            tutorials_list = list(Tutorial.objects.filter(
                tutorial_title__contains=query,
                tutorial_is_private=0))
        if not query:
            title = "Nie podano żadnej wartości"
            return render(request, self.template_name, {'list_title': title})

        return render(request, self.template_name, {'page_obj_posts': posts_list,
                                                    'page_obj_tutorials': tutorials_list,
                                                    'list_title': title,
                                                    'query': query})
