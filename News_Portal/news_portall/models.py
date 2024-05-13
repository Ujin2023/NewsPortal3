from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    author_rat = models.IntegerField(default = 0)

    def update_rating(self):
        author_post_rat = 0
        author_comment_rat = 0
        comment_author_rat = 0
        post = Post.objects.filter(author = self)
        for p in post:
            author_post_rat += p.post_rat
        comments = Comment.objects.filter(user_comment = self.user)
        for c in comments:
            author_comment_rat += c.comment_rat
        post_comment = Comment.objects.filter(post_comment__author = self)
        for pc in post_comment:
            comment_author_rat += pc.comment_rat
        self.author_rat = author_post_rat * 3 + author_comment_rat + comment_author_rat
        self.save()

    def __str__(self):
        return self.user.username



class Category(models.Model):
    category_theme = models.CharField(max_length = 30, unique = True)

class Post(models.Model):
    stat = "stat"
    news = "news"
    CHOICE = [(stat, "Статья"), (news, "Новости")]
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    snpost = models.CharField(max_length=10, choices=CHOICE, default=news)
    post_cat = models.ManyToManyField(Category, through="PostCategory")
    post_head = models.CharField(max_length=50)
    post_rat = models.IntegerField(default=0)
    post_text = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

    def like(self):
        self.post_rat += 1
        self.save()
    def dislike(self):
        self.post_rat -= 1
        self.save()

    def preview(self):
        return self.post_text[:124] + "..."

    def __str__(self):
        return f'{self.post_head.title()}: {self.post_text[:20]}'

    def get_absolute_url(self):
        return reverse('default', args=[str(self.id)])

class PostCategory(models.Model):
    post_category = models.ForeignKey(Post, on_delete = models.CASCADE)
    category_post = models.ForeignKey(Category, on_delete = models.CASCADE)

class Comment(models.Model):
    post_comment = models.ForeignKey(Post, on_delete = models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add = True)
    comment_rat = models.IntegerField(default = 0)
    comment_text = models.TextField()
    user_comment = models.ForeignKey(User, on_delete = models.CASCADE)

    def like(self):
        self.comment_rat += 1
        self.save()
    def dislike(self):
        self.comment_rat -= 1
        self.save()