from django.urls import path, include
from .views import HomePageView, CreatePostView

app_name='posts'

urlpatterns = [
    path('', HomePageView.as_view() , name='home' ),
    path('add/', CreatePostView.as_view(), name='add_post'),
]
