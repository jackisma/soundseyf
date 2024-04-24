from django.contrib.sitemaps import Sitemap
from django.db.models.base import Model
from blog.models import Post
from django.urls import reverse


class BlogStaticSitemap(Sitemap):
    priority = 0.5
    changefreq = "weekly"

    def items(self):
        return ["blog:blog-home"]

    def location(self, item):
        return reverse(item)




class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.filter(status='p')

    def lastmod(self, obj):
        return obj.published_on

    def location(self,item):
        return reverse('blog:blog-single',kwargs={'slug':item.slug})