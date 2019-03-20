from django.contrib.syndication.views import Feed
from .models import Post

class AllPostRssFeed(Feed):
    title="PureDark233's Blog"

    link='/'
    descriptions="Posts"

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return '[%s] %s'%(item.category, item.title)
    def item_description(self, item):
        return item.body