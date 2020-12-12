from django.contrib import admin

# Register your models here.

from .models import Post, Category, Tutorial

admin.site.register([Post, Category, Tutorial])
