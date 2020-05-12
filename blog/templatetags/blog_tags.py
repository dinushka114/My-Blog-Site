from django import template
from ..models import Post
from ..models import Category

register = template.Library()

@register.inclusion_tag('blog/latest-post.html')
def show_latest_post(count=5):
        latest_posts = Post.objects.filter(status='published').order_by('-publish')[:count]
        return {'latest_posts':latest_posts}

@register.simple_tag
def total_posts():
    return Post.objects.filter(status = 'published').count()
