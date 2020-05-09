from haystack import indexes
from blog.models import Post
import datetime


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    """
    Haystack Post search index
    """
    text = indexes.CharField(document=True, use_template=True)
    publish = indexes.DateTimeField(model_attr='publish', null=True)
    # is_featured = indexes.BooleanField(model_attr='is_featured')
    content_auto = indexes.EdgeNgramField(model_attr='title')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
