from django.contrib import admin
from .models import Post, Contact, GymClass, Trainer, ClassEnrollment

admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(GymClass)
admin.site.register(Trainer)
admin.site.register(ClassEnrollment)
