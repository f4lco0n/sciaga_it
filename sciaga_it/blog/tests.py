from django.test import SimpleTestCase
from django.test import TestCase, Client
from .models import Category, Post, User
import json
from django.urls import resolve, reverse
from .views import HomeView, PostDetailView, PostListView, \
    PostCreateView, UpdatePostView, DeletePostView, category_view, \
    show_user_post_view, show_user_profile_view, TutorialListView, \
    TutorialDetailView, TutorialCreateView, TutorialUpdateView, \
    DeleteTutorialView


class TestUrls(SimpleTestCase):
    # POSTS

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, HomeView)

    def test_post_details_resolves(self):
        url = reverse('post-details', args=[1])
        self.assertEquals(resolve(url).func.view_class, PostDetailView)

    def test_post_lists_resolves(self):
        url = reverse('post_list')
        self.assertEquals(resolve(url).func.view_class, PostListView)

    def test_add_post_resolves(self):
        url = reverse('add_post')
        self.assertEquals(resolve(url).func.view_class, PostCreateView)

    def test_edit_post_resolves(self):
        url = reverse('update-post', args=[1])
        self.assertEquals(resolve(url).func.view_class, UpdatePostView)

    def test_delete_post_resolves(self):
        url = reverse('delete-post', args=[1])
        self.assertEquals(resolve(url).func.view_class, DeletePostView)

    def test_category_view_resolves(self):
        url = reverse('category', args=['programowanie'])
        self.assertEquals(resolve(url).func, category_view)

    def test_user_post_view_resolves(self):
        url = reverse('user_posts', args=['f4lco0n'])
        self.assertEquals(resolve(url).func, show_user_post_view)

    def test_user_profile_view_resolves(self):
        url = reverse('user_profile', args=['f4lco0n'])
        self.assertEquals(resolve(url).func, show_user_profile_view)

    # TUTORIALS

    def test_tutorial_list_resolves(self):
        url = reverse('tutorial_list')
        self.assertEquals(resolve(url).func.view_class, TutorialListView)

    def test_tutorial_details_resolves(self):
        url = reverse('tutorial-details', args=[1])
        self.assertEquals(resolve(url).func.view_class, TutorialDetailView)

    def test_add_tutorial_resolves(self):
        url = reverse('add_tutorial')
        self.assertEquals(resolve(url).func.view_class, TutorialCreateView)

    def test_update_tutorial_resolves(self):
        url = reverse('update-tutorial', args=[1])
        self.assertEquals(resolve(url).func.view_class, TutorialUpdateView)

    def test_delete_tutorial_resolves(self):
        url = reverse('delete-tutorial', args=[1])
        self.assertEquals(resolve(url).func.view_class, DeleteTutorialView)


class TestViews(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='programowanie'
        )
        self.user = User.objects.create(
            username='testuser',
            password='testpassword'
        )
        self.post1 = Post.objects.create(
            title='sciaga1',
            category=self.category,
            title_tag='#1',
            author=self.user,
            short_description='opis testowy',
            body='dlugi opis testowy',
            is_private=0
        )

    def test_post_create_POST(self):
        url = reverse('add_post')
        response = self.client.post(url, {
            'title': 'sciaga2',
            'category': 1,
            'title_tag': 'sciaga #2',
            'author': 1,
            'short_description': 'druga sciaga',
            'body': 'opis sciagi drugiej',
            'is_private': 0,

        })

        post2 = Post.objects.get(id=2)
        # assert if created post is saved correctly
        self.assertEquals(post2.title, 'sciaga2')
        self.assertEquals(post2.is_private, 0)
        self.assertEquals(post2.body, 'opis sciagi drugiej')
        category_test = Category.objects.get(id=1)
        # assert if category is saved correctly
        self.assertEquals(category_test.id, post2.category_id)
        self.assertEquals(category_test.name, 'programowanie')
