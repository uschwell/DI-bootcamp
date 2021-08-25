from django.contrib import admin

# Register your models here.
from .models import Category, Gif


admin.site.register(Gif)
admin.site.register(Category)
