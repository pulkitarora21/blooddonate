from django.conf.urls import patterns, include, url
from views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blooddonation.views.home', name='home'),
    # url(r'^blooddonation/', include('blooddonation.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='home'),
    url(r'^register/', include('register.urls')),
    url(r'^welcome/', welcome, name='welcome'),
    url(r'^logout/', logout, name='logout'),
    url('', include('social.apps.django_app.urls', namespace='social'))
)
