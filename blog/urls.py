from django.urls import path
from .views import PostListView , PostDetailView , TagIndexView  , about , BlogSearchListView
from .feeds import LatestPostsFeed

app_name = 'blog'
urlpatterns = [
    path('' , PostListView.as_view() , name='index'),
    path('tag/<slug>' , TagIndexView.as_view() , name='tagged'),
    path('search/' , BlogSearchListView.as_view() , name = 'blog-search'),
    path('post/<int:year>/<int:month>/<int:day>/<slug>/<int:pk>' , PostDetailView.as_view() , name='post-detail'),
    path('feed/' , LatestPostsFeed() , name = 'post_feed'),
    path('about/', about , name = 'about' ),

    # path('archive/<int:year>/<int:month>' , BlogMonthArchiveView.as_view() , name = 'month_archive')
]
