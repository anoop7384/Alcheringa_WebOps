from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    description = models.TextField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='base.jpg',upload_to='posts_pics')
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.author.username} {self.date_posted}'
        
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_commented = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.author.username} {self.date_commented}'

    class Meta:
        ordering = ['date_commented']
