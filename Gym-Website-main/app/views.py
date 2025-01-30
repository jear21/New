from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, DetailView, DeleteView
from .models import Post, Contact
from django.views.generic.edit import CreateView, UpdateView
from .forms import ContactForm

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class BlogListView(ListView):
    model = Post
    context_object_name ='posts'
    template_name ='app/blog_list.html'

class BlogDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name ='app/blog_detail.html'
    

class ContactPageView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'app/contact.html'
    success_url = reverse_lazy('home')

