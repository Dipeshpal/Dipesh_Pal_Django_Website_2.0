from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from Dipesh_Pal.utils import unique_slug_generator
from cloudinary.models import CloudinaryField


# Create your models here.
class Home(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    body = models.TextField()
    CATEGORY_CHOICES = [
        ('NEWS', 'News'),
        ('ANDROID', 'Android'),
        ('PC', 'PC'),
        ('Machine Learning', 'Machine Learning'),
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
    thumbnail = CloudinaryField('image')
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


class Comment(models.Model):
    Post = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='comments')
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Body = models.TextField()
    Created = models.DateTimeField(auto_now_add=True)
    Active = models.BooleanField(default=True)
    Parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    class Meta:
        ordering = ('Created',)

    def __str__(self):
        return 'Comment By {}'.format(self.Name)
