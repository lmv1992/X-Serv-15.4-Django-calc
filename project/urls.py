from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'project.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),
	url(r'(\d+)\+(\d+)$', "calc.views.sumar"),
	url(r'(\d+)-(\d+)$', "calc.views.restar"),
	url(r'(\d+)\*(\d+)$', "calc.views.multiplicar"),
	url(r'(\d+)/(\d+)$', "calc.views.dividir"),
	url(r'^admin/', include(admin.site.urls)),
	url(r'.*', "calc.views.error"),
)
