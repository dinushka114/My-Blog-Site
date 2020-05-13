from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views.generic import ListView , DetailView ,TemplateView
from .models import Post
from .models import Category
from taggit.managers import TaggableManager
from taggit.models import Tag
from django.db.models import Q


class TagMixin(object):
    def get_context_data(self,**kwargs):
        context = super(TagMixin , self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

class CategoryMixin(object):
    def get_context_data(self, **kwargs):
        context = super(CategoryMixin , self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class AboutView(CategoryMixin , TagMixin , TemplateView):
    template_name = 'blog/about.html'

class ProjectsView(CategoryMixin , TagMixin , TemplateView):
    template_name = 'blog/projects.html'

class PostListView(CategoryMixin , TagMixin , ListView):
    model = Post
    template_name = 'blog/index.html'
    paginate_by = 7
    context_object_name = 'posts'
    queryset = Post.objects.filter(status='published').order_by('-publish')

class PostDetailView( CategoryMixin , TagMixin , DetailView):
    model = Post
    template_name = 'blog/post-detail.html'


class TagIndexView(CategoryMixin , TagMixin , ListView):
    model = Post
    template_name = 'blog/tags-view.html'
    context_object_name = 'posts'
    paginate_by = 7
    def get_queryset(self):
        # posts = Post.objects.filter(status = 'published')
        return Post.objects.filter(status='published' , tags__slug=self.kwargs.get('slug')).order_by('-publish')

class CategoryIndexView(CategoryMixin , TagMixin , ListView):
    model = Post
    template_name = 'blog/category-view.html'
    paginate_by = 7
    def get_queryset(self):
        return Post.objects.filter(status = 'published' ,category=self.kwargs.get('cat'))

class BlogSearchListView(CategoryMixin , TagMixin ,ListView):
    model  = Post
    # paginate_by = 10
    template_name = 'blog/search.html'
    context_object_name = 'posts'
    def get_queryset(self):
        keywords = self.request.GET.get('query')
        if(keywords):
            # posts = Post.objects.filter(status = 'published', Q(title__icontains=keywords)|Q(body__icontains=keywords))
            posts = Post.objects.filter(status = 'published')
            # posts = Post.objects.filter(status='published' and Q(title__icontains=keywords)|Q(body__icontains=keywords))

            return posts.filter(Q(title__icontains=keywords)|Q(body__icontains=keywords))
