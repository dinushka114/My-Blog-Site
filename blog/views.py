from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views.generic import ListView , DetailView ,TemplateView
from .models import Post
from taggit.managers import TaggableManager
from taggit.models import Tag
from django.db.models import Q


class TagMixin(object):
    def get_context_data(self,**kwargs):
        context = super(TagMixin , self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

class AboutView(TagMixin , TemplateView):
    template_name = 'blog/about.html'

class ProjectsView(TagMixin , TemplateView):
    template_name = 'blog/projects.html'

class PostListView(TagMixin , ListView):
    model = Post
    template_name = 'blog/index.html'
    paginate_by = 4
    context_object_name = 'posts'

class PostDetailView(TagMixin , DetailView):
    model = Post
    template_name = 'blog/post-detail.html'


class TagIndexView(TagMixin , ListView):
    model = Post
    template_name = 'blog/category-view.html'
    context_object_name = 'posts'
    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('slug'))

class BlogSearchListView(TagMixin ,ListView):
    model  = Post
    # paginate_by = 10
    template_name = 'blog/search.html'
    context_object_name = 'posts'
    def get_queryset(self):
        keywords = self.request.GET.get('query')
        if(keywords):
            posts = Post.objects.filter(
            Q(title__icontains=keywords)|
            Q(body__icontains=keywords)
            )
            return posts
