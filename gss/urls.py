from django.conf.urls import patterns, include, url

from gss import views
from gss.api import TelecommandResource

from tastypie.api import Api

tc_api = Api(api_name='tc')
tc_api.register(TelecommandResource())

urlpatterns = [
    url(r'^q/$', views.telecommands, name='telecommand_home'),
    url(r'^login/$', views.telecommands, name='keam_login'),
    # url(r'^logout/$', views.user_logout, name='keam_logout'),
]

urlpatterns += (
	url(r'api/', include(tc_api.urls)),
)