from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CASCADE

User = get_user_model()


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE, related_name='posts')
    description = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE, related_name='likes', verbose_name='likes owner')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='like', verbose_name='post')
    like = models.BooleanField('like', default=False)

    def __str__(self):
        return f'{self.post} {self.like}'


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Image(models.Model):
    image = models.ImageField(upload_to='posts')
    post = models.ForeignKey(Post, on_delete=CASCADE, related_name='images')


class Favorite(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='favorites')
    favorite = models.BooleanField('favorite', default=False)

    def __str__(self):
        return f'{self.owner} {self.post}'


class Contact(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
