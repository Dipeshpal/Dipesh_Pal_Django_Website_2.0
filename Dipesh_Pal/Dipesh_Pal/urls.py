from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from home.sitemaps import PostSitemap, StaticViewSitemap
from django.contrib.sitemaps.views import sitemap
from django.conf.urls import url


sitemaps = {
    'posts': PostSitemap,
    'static': StaticViewSitemap(['sitemap',
                                 'home:home',
                                 'home:News', 'home:android', 'home:PC', 'home:Others', 'home:create',
                                 'about:about',
                                 'disclaimer:disclaimer',
                                 'contact_us:contact_us',
                                 'videos:videos_page',
                                 ]),
}


urlpatterns = [
    url('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    url(r'^admin/', admin.site.urls),
    path('', include('home.urls'), name='home'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('about/', include('about.urls'), name='about'),
    path('disclaimer/', include('disclaimer.urls'), name='disclaimer'),
    path('privacy_policy/', include('privacy_policy.urls')),
    path('contact_us/', include('contact_us.urls'), name='contact_us'),
    path('videos/', include('videos.urls'), name='videos'),
]


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
