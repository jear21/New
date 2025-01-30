from django.urls import path
from . import views

urlpatterns = [
    # Post CRUD
    path('blog/', views.PostListView.as_view(), name='post_list'),
    path('blog/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('blog/new/', views.PostCreateView.as_view(), name='post_create'),
    path('blog/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('blog/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    # Gym Class CRUD
    path('classes/', views.GymClassListView.as_view(), name='gym_class_list'),
    path('classes/<int:pk>/', views.GymClassDetailView.as_view(), name='gym_class_detail'),
    path('classes/new/', views.GymClassCreateView.as_view(), name='gym_class_create'),
    path('classes/<int:pk>/edit/', views.GymClassUpdateView.as_view(), name='gym_class_edit'),
    path('classes/<int:pk>/delete/', views.GymClassDeleteView.as_view(), name='gym_class_delete'),

    # Trainer CRUD
    path('trainers/', views.TrainerListView.as_view(), name='trainer_list'),
    path('trainers/<int:pk>/', views.TrainerDetailView.as_view(), name='trainer_detail'),
    path('trainers/new/', views.TrainerCreateView.as_view(), name='trainer_create'),
    path('trainers/<int:pk>/edit/', views.TrainerUpdateView.as_view(), name='trainer_edit'),
    path('trainers/<int:pk>/delete/', views.TrainerDeleteView.as_view(), name='trainer_delete'),

    # Class Enrollment CRUD
    path('enrollments/', views.ClassEnrollmentListView.as_view(), name='class_enrollment_list'),
    path('enroll/<int:gym_class_id>/', views.ClassEnrollmentCreateView.as_view(), name='class_enroll'),
    path('enrollments/<int:pk>/delete/', views.ClassEnrollmentDeleteView.as_view(), name='class_enrollment_delete'),

    # Contact Form
    path('contact/', views.ContactCreateView.as_view(), name='contact'),
]
