from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def str(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    author =models.ForeignKey("auth.User", on_delete=models.CASCADE)
    body = models.TextField()

    def str(self):
        return self.title


    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={"pk": self.pk})
    
class GymClass(models.Model):
    name = models.CharField(max_length=200)  # E.g., Yoga, Zumba, Pilates, etc.
    description = models.TextField()
    max_capacity = models.PositiveIntegerField()
    available_spots = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def spots_available(self):
        return self.available_spots


# Model for Trainers (Instructors)
class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    specialty = models.CharField(max_length=200)  # E.g., Weight training, Yoga, etc.

    def __str__(self):
        return self.user.username

# Model for Member Enrollment in Classes
class ClassEnrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class_schedule = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(default=timezone.now)
