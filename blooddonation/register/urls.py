from django.conf.urls import patterns, url
from register import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^request$', views.raiserequest, name='request'),
	url(r'^volunteer$', views.volunteer, name='volunteer'),
	url(r'^drive$', views.drive, name='drive'),
	
#	url(r'^profile/$', views.profile, name='profile'),
#	url(r'^apply/$', views.apply, name='apply'),
)
