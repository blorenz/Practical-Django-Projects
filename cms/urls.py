from django.conf.urls.defaults import patterns, include, url

from coltrane.models import Entry

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

entry_info_dict = {
		'queryset': Entry.objects.all(),
		'date_field': 'pub_date',
		}

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
    url(r'^weblog/$', 'django.views.generic.date_based.archive_index',
	    	entry_info_dict),
    url(r'^weblog/(?P<year>\d{4})/$',
	    	'django.views.generic.date_based.archive_year',
	    	entry_info_dict),
    url(r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/$',
	    	'django.views.generic.date_based.archive_month',
	    	entry_info_dict),
    url(r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})',
	    	'django.views.generic.date_based.archive_day',
	    	entry_info_dict),
    url(r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'django.views.generic.date_based.object_detail', entry_info_dict),
    url(r'', include('django.contrib.flatpages.urls')),
    )

