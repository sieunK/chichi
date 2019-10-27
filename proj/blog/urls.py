from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('Blog', views.BlogViewSet)
router.register('BlogPic', views.BlogPicViewSet)
router.register('BlogFile', views.BlogFileViewSet)

urlpatterns = {
    path('',include(router.urls))
}