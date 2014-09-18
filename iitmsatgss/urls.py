from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iitmsatgss.views.home', name='home'),
    url(r'^telecommands/$', 'gss.views.telecommands', name='new_telecommand'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
