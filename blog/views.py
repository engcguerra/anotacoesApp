#from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Post
from .forms import PostForm

# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'posts/home.html'

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/adicionar.html'
    success_url = reverse_lazy('posts:home')
