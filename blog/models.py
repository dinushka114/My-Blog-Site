from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from PIL import Image

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class Post(models.Model):
    STATUS_CHOICES = (
            ('draft', 'Draft'),
            ('published', 'Published'),
                )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    category = models.ForeignKey(Category , on_delete = models.CASCADE)
    image = models.ImageField( blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_post')
    body = RichTextUploadingField('content')
    meta_description = models.TextField(max_length=160 , blank=True)
    tags = TaggableManager()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length = 10 , choices=STATUS_CHOICES , default='draft')

    class meta:
        ordering = ('-publish')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post-detail',
                                        kwargs={
                                        'year':self.publish.year,
                                        'month':self.publish.month,
                                        'day':self.publish.day,
                                        'pk': self.pk,
                                        'slug':self.slug
                                        })
