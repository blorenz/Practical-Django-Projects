from django.conf.urls.defaults import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cms.views.home', name='home'),
    # url(r'^cms/', include('cms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/(?P<path>.*)$', 'django.views.static.serve', 
	    { 'document_root': '/virtualenvs/pdp/pdp/tinymce/' }),
    url(r'^search/$', 'cms.search.views.search'),
    (r'^weblog/categories/', include('coltrane.urls.categories')),
    (r'^weblog/links/', include('coltrane.urls.links')),
    (r'^weblog/tags', include('coltrane.urls.tags')),
    (r'^weblog/', include('coltrane.urls.entries')),
    url(r'', include('django.contrib.flatpages.urls')),
    )

