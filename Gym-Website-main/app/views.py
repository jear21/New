from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, GymClass, Trainer, ClassEnrollment, Contact
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages

# Post Views (CRUD)
class PostListView(ListView):
    model = Post
    template_name = 'app/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'app/post_detail.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    template_name = 'app/post_form.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Post created successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_list')

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'app/post_form.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        messages.success(self.request, 'Post updated successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'app/post_confirm_delete.html'
    context_object_name = 'post'

    def get_success_url(self):
        messages.success(self.request, 'Post deleted successfully!')
        return reverse_lazy('post_list')

# GymClass Views (CRUD)
class GymClassListView(ListView):
    model = GymClass
    template_name = 'app/gym_class_list.html'
    context_object_name = 'classes'

class GymClassDetailView(DetailView):
    model = GymClass
    template_name = 'app/gym_class_detail.html'
    context_object_name = 'gym_class'

class GymClassCreateView(CreateView):
    model = GymClass
    template_name = 'app/gym_class_form.html'
    fields = ['name', 'description', 'max_capacity', 'available_spots']

    def form_valid(self, form):
        messages.success(self.request, 'Gym class created successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('gym_class_list')

class GymClassUpdateView(UpdateView):
    model = GymClass
    template_name = 'app/gym_class_form.html'
    fields = ['name', 'description', 'max_capacity', 'available_spots']

    def form_valid(self, form):
        messages.success(self.request, 'Gym class updated successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('gym_class_list')

class GymClassDeleteView(DeleteView):
    model = GymClass
    template_name = 'app/gym_class_confirm_delete.html'
    context_object_name = 'gym_class'

    def get_success_url(self):
        messages.success(self.request, 'Gym class deleted successfully!')
        return reverse_lazy('gym_class_list')
    
# Trainer Views (CRUD)
class TrainerListView(ListView):
    model = Trainer
    template_name = 'app/trainer_list.html'
    context_object_name = 'trainers'

class TrainerDetailView(DetailView):
    model = Trainer
    template_name = 'app/trainer_detail.html'
    context_object_name = 'trainer'

class TrainerCreateView(CreateView):
    model = Trainer
    template_name = 'app/trainer_form.html'
    fields = ['user', 'bio', 'specialty']

    def form_valid(self, form):
        messages.success(self.request, 'Trainer created successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('trainer_list')

class TrainerUpdateView(UpdateView):
    model = Trainer
    template_name = 'app/trainer_form.html'
    fields = ['user', 'bio', 'specialty']

    def form_valid(self, form):
        messages.success(self.request, 'Trainer updated successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('trainer_list')

class TrainerDeleteView(DeleteView):
    model = Trainer
    template_name = 'app/trainer_confirm_delete.html'
    context_object_name = 'trainer'

    def get_success_url(self):
        messages.success(self.request, 'Trainer deleted successfully!')
        return reverse_lazy('trainer_list')

# Class Enrollment Views (CRUD)
class ClassEnrollmentListView(ListView):
    model = ClassEnrollment
    template_name = 'app/class_enrollment_list.html'
    context_object_name = 'enrollments'

class ClassEnrollmentCreateView(CreateView):
    model = ClassEnrollment
    template_name = 'app/class_enrollment_form.html'
    fields = ['user', 'gym_class']

    def form_valid(self, form):
        gym_class = form.cleaned_data['gym_class']
        if gym_class.available_spots > 0:
            gym_class.available_spots -= 1
            gym_class.save()
            form.instance.user = self.request.user
            messages.success(self.request, f'You have successfully enrolled in {gym_class.name}')
            return super().form_valid(form)
        else:
            messages.error(self.request, 'No spots available for this class.')
            return redirect('gym_class_list')

    def get_success_url(self):
        return reverse_lazy('gym_class_list')

class ClassEnrollmentDeleteView(DeleteView):
    model = ClassEnrollment
    template_name = 'app/class_enrollment_confirm_delete.html'
    context_object_name = 'enrollment'

    def get_success_url(self):
        enrollment = self.get_object()
        gym_class = enrollment.gym_class
        gym_class.available_spots += 1
        gym_class.save()
        messages.success(self.request, 'Your enrollment has been cancelled.')
        return reverse_lazy('gym_class_list')
    
# Contact Views (CRUD)
class ContactCreateView(CreateView):
    model = Contact
    template_name = 'app/contact_form.html'
    fields = ['name', 'email', 'message']
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        messages.success(self.request, 'Your message has been sent successfully!')
        return super().form_valid(form)