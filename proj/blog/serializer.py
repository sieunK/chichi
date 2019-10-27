from rest_framework import serializers
from .models import Blog, BlogFile, BlogPic

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Blog
        fields = ('pk', 'title', 'body', 'author',)

class BlogPicSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    myimage = serializers.ImageField(use_url=True)

    class Meta:
        model = BlogPic
        fields = ('pk', 'author', 'myimage', 'desc',)

class BlogFileSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    myfile = serializers.FileField(use_url=True)

    class Meta:
        model = BlogFile
        fields = ('pk', 'author', 'myfile', 'desc',)