from django.contrib.sitemaps import Sitemap
from home.models import Home
from django.urls import reverse
from datetime import datetime


class PostSitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.5

    def items(self):
        return Home.objects.all()

    def lastmod(self, obj):
        return obj.pub_date


class StaticViewSitemap(Sitemap):
    def __init__(self, names):
        self.names = names

    def items(self):
        return self.names

    def changefreq(self, obj):
        return 'weekly'

    def lastmod(self, obj):
        return datetime.now()

    def location(self, obj):
        return reverse(obj)
    # priority = 0.5
    # changefreq = 'hourly'
    # def items(self):
    #     return ['sitemap']
    #
    # def location(self, item):
    #     return reverse(item)
