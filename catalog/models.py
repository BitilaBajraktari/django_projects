from datetime import date

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a Blogs Genre')

    def __str__(self):
        return self.name


class Bloggers(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=400, help_text="Enter your bio details here.")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ["user", "bio"]

    def get_absolute_url(self):
        return reverse('blogs_by_bloggers', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Blogs(models.Model):
    title = models.CharField(max_length=200)
    bloggers = models.ForeignKey('Bloggers', on_delete=models.SET_NULL, null=True)
    genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter you blog text here.")
    post_date = models.DateField(default=date.today)

    class Meta:
        ordering = ["-post_date"]

    def get_absolute_url(self):
        return reverse('blogs-detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class Comment(models.Model):
    description = models.TextField(max_length=1000, help_text="Enter comment about blog here.")
    bloggers = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    blogs = models.ForeignKey(Blogs, on_delete=models.CASCADE)

    class Meta:
        ordering = ["post_date"]

    def __str__(self):

        len_title = 75
        if len(self.description) > len_title:
            titlestring = self.description[:len_title] + '...'
        else:
            titlestring = self.description
        return titlestring
