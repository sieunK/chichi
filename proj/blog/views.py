from django.shortcuts import render
from .models import Blog, BlogPic, BlogFile
from .serializer import BlogFileSerializer, BlogPicSerializer, BlogSerializer

from rest_framework import viewsets

from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('id')
    serializer_class = BlogSerializer

    filter_backends = [SearchFilter]
    search_fields = ('title',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none()
        return qs

class BlogPicViewSet(viewsets.ModelViewSet):
    queryset = BlogPic.objects.all().order_by('id')
    serializer_class = BlogPicSerializer

class BlogFileViewSet(viewsets.ModelViewSet):
    queryset = BlogFile.objects.all().order_by('id')
    serializer_class = BlogFileSerializer
  
class Mypatination(PageNumberPagination):
    page_size = 100