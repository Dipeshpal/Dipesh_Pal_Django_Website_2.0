from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from Dipesh_Pal.utils import unique_slug_generator


# Create your models here.
class Home(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    body = models.TextField()
    CATEGORY_CHOICES = [
        ('NEWS', 'News'),
        ('ANDROID', 'Android'),
        ('PC', 'PC'),
        ('OFFERS', 'Offers'),
        ('OTHERS', 'Others'),
    ]
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='OTHERS',
    )

    link = models.URLField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:100]+'...'

    def get_absolute_url(self):
        return '/' + self.title


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=Home)
