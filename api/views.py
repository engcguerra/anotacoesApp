# from django.shortcuts import render

# Create your views here.
# from django.contrib.auth.models import Group, User

from rest_framework import permissions, viewsets
from tutorial.quickstart.serializers import GroupSerializer, UserSerializer

from blog.models import Post
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

# class PostViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Post.objects.all().order_by('id')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.AllowAny]



# class ExampleView(APIView):
#     permission_classes = [AllowAny]
#     queryset = Post.objects.all().order_by('id')
    
#     def get(self, request, format=None):
#         content = {
#             'status': 'request was permitted'
#         }
#         return Response(content)
    
from rest_framework import generics
from .serializers import PostSerializer

# class PostListCreate(generics.ListCreateAPIView):
class PostListCreate(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "pk"