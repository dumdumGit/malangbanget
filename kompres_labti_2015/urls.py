"""kompres_labti_2015 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls import patterns,include,url
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from app_kompres.views import mysitemap
from app_kompres.models import article
admin.autodiscover()
#  <title>.
admin.site.site_title = 'Tim MalangBanget'


admin.site.site_header = 'Admin Site MalangBanget'

#  admin index page.
admin.site.index_title = 'Administration Console'

info_dict = {
    'queryset': article.objects.all(),
    
}

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app_kompres.views.index'),
    url(r'^$','app_kompres.views.func_wisata'),
    (r'^', include('app_kompres.urls')),
	(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^sitemap\.xml$',sitemap,{'sitemaps':{'blog':GenericSitemap(info_dict, priority=0.6)}},name='django.contrib.sitemaps.views.sitemap'),
    url(r'^sitemap/$', mysitemap, name='mysitemap'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



