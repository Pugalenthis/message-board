from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


# posts/views.py


class HomePageView(ListView):
    model = Post
    template_name = "home.html"