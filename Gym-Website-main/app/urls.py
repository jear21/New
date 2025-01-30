from django.urls import path
from .views import (HomePageView, AboutPageView, BlogListView, BlogDetailView, ContactPageView)
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('blog/',BlogListView.as_view(), name='blog'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('Contact/', ContactPageView.as_view(), name='Contact'),
    

]

