from django.contrib.sitemaps import Sitemap
from django.db.models.base import Model
from music.models import Composer , MasterPiece
from django.urls import reverse

class ComposerSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.1

    def items(self):
        return ["music:composers"]

    def location(self, item):
        return reverse(item)
    



class PiecesSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.1

    def items(self):
        return MasterPiece.objects.all()

    def location(self,item):
        return reverse('music:pieces',kwargs={'cid':item.pk})