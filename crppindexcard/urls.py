from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # url to form login
    url(r'^accounts/login/$', 'crppindexcard.views.my_login', name="my_login"),
    # url to logout page
    url(r'^logout/$', 'crppindexcard.views.my_logout', name='logout'),

    # url to page with index card (lis of sections) of authenticated user/city
    url(r'^index/', 'crppindexcard.views.index', name='index'),

    # url to page with questions from a specified section
    url(r'^questions/(?P<index_card_id>\d+)/(?P<section_id>\d+)/$', 'crppindexcard.views.section_questions', name='questions'),

    # url to admin pages
    url(r'^admin/', include(admin.site.urls)),
)

