from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # url to form login
    url(r'^accounts/login/$', 'crppindexcard.views.my_login', name="my_login"),
    # url to logout page
    url(r'^logout/$', 'crppindexcard.views.my_logout', name='logout'),

    # url to page with index card (lis of sections) of authenticated user
    url(r'^index/', 'crppindexcard.views.index', name='index'),

    # url to admin pages
    url(r'^admin/', include(admin.site.urls)),
)

