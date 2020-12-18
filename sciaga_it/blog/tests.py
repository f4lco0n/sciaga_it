from django.test import SimpleTestCase
from django.urls import resolve, reverse
from .views import HomeView, PostDetailView, PostListView, \
    PostCreateView, UpdatePostView, DeletePostView, category_view, \
    show_user_post_view, show_user_profile_view, TutorialListView,\
    TutorialDetailView, TutorialCreateView, TutorialUpdateView,\
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