from django.urls import path
from .views import PostListView , PostDetailView , TagIndexView  , BlogSearchListView , AboutView , ProjectsView , CategoryIndexView
from .feeds import LatestPostsFeed

app_name = 'blog'
urlpatterns = [
    path('' , PostListView.as_view() , name='index'),
    path('tag/<slug>' , TagIndexView.as_view() , name='tagged'),
    path('category/<cat>' ,CategoryIndexView.as_view() , name='categories' ),
    path('search/' , BlogSearchListView.as_view() , name = 'blog-search'),
    path('post/<int:year>/<int:month>/<int:day>/<slug>/<int:pk>' , PostDetailView.as_view() , name='post-detail'),
    path('feed/' , LatestPostsFeed() , name = 'post_feed'),
    path('about/', AboutView.as_view() , name = 'about' ),
    path('projects/' , ProjectsView.as_view() , name = 'projects'),

    # path('archive/<int:year>/<int:month>' , BlogMonthArchiveView.as_view() , name = 'month_archive')
]
