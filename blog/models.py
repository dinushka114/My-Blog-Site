from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from tinymce import HTMLField
from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    image = models.ImageField( blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_post')
    body = HTMLField('content')
    meta_description = models.TextField(max_length=160 , blank=True)
    tags = TaggableManager()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class meta:
        ordering = ('-publish')

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('blog:detail',
    #                    args=[
    #                        self.publish.year,
    #                        self.publish.month,
    #                        self.publish.day,
    #                        self.slug,
    #                        self.id])

    def get_absolute_url(self):
        return reverse('blog:post-detail',
                                        kwargs={
                                        'year':self.publish.year,
                                        'month':self.publish.month,
                                        'day':self.publish.day,
                                        'pk': self.pk,
                                        'slug':self.slug
                                        })
