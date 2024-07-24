from blog.models import Post
# from rest_framework import routers, serializers, viewsets
# from django.contrib.auth.models import User
from rest_framework import serializers

#class PostSerializer(serializers.HyperlinkedModelSerializer):
# Serializers define the API representation.
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['titulo', 'imagem']
