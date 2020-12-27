from django.contrib import admin

# Register your models here.

from .models import Post, Category, Tutorial, Profile

admin.site.register([Post, Category, Tutorial, Profile])
