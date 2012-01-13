from django.conf.urls.defaults import *

from coltrane.models import Category 

urlpatterns = patterns('coltrane.views',
		(r'^$', 
			'django.views.generic.list_detail.object_list',
			{ 'queryset': Category.object.all() }),
		(r'^(?P<slug>[-\w]+)/$', 
			'coltrane.views.category_detail'),
		)

