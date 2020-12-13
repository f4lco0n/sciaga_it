from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime, date


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='')
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    short_description = models.CharField(max_length=255,
                                         default='Kliknij link powyżej aby zobaczyć post')
    body = RichTextUploadingField(blank=True, config_name='special')
    is_private = models.BooleanField(default=False)
    publication_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('post_list')


class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=255)
    tutorial_category = models.ForeignKey(Category, on_delete=models.CASCADE, default='')
    tutorial_title_tag = models.CharField(max_length=255)
    tutorial_author = models.ForeignKey(User, on_delete=models.CASCADE)
    tutorial_short_description = models.CharField(max_length=255,
                                         default='Kliknij link powyżej aby zobaczyć tutorial')
    tutorial_body = RichTextUploadingField(blank=True, config_name='special')
    tutorial_publication_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.tutorial_title + '|' + str(self.tutorial_author)


    def get_absolute_url(self):
        return reverse('tutorial_list')


