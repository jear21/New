# Generated by Django 5.1.4 on 2025-01-29 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='membership_type',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='registration_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
