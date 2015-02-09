from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # url to form login
    url(r'^accounts/login/$', 'crppindexcard.views.my_login', name="my_login"),

    # url to logout page
    url(r'^logout/$', 'crppindexcard.views.my_logout', name='logout'),

    # base url
    url(r'^$', 'crppindexcard.views.index', name='index'),

    # url to copyright page
    url(r'^copyright/$', 'crppindexcard.views.copyright', name='copyright'),

    # url to page with index card (lis of sections) of authenticated user/city
    url(r'^index/', 'crppindexcard.views.index', name='index'),

    # url to page with questions from a specified section
    url(r'^questions/(?P<index_card_id>\d+)/(?P<section_id>\d+)/$', 'crppindexcard.views.section_questions', name='questions'),

    # url to page with questions from a specified hazard
    url(r'^hazard_questions/(?P<index_card_id>\d+)/(?P<hazard_id>\d+)/$', 'crppindexcard.views.hazard_questions', name='hazard_questions'),

    # url to page with list of services of an city
    url(r'^services_list/(?P<index_card_id>\d+)/(?P<hazard_id>\d+)/$', 'crppindexcard.views.services_list', name='services_list'),

    # url to page with questions from a services disruption hazard
    url(r'^service_questions/(?P<index_card_id>\d+)/(?P<hazard_id>\d+)/(?P<index_card_service_id>\d+)/$', 'crppindexcard.views.service_questions', name='service_questions'),

    # url to page with questions for infrastructures related to services supply
    url(r'^competence_questions/(?P<index_card_id>\d+)/(?P<index_card_competence_category_id>\d+)/$', 'crppindexcard.views.competence_questions', name='competence_questions'),

    # url to page with questions for infrastructures related to services supply
    url(r'^infrastructure_questions/(?P<index_card_id>\d+)/(?P<element_id>\d+)/$', 'crppindexcard.views.infrastructure_questions', name='infrastructure_questions'),


    #url test element questions
    url(r'^test/', 'crppindexcard.views.test', name='test'),

    # url to admin pages
    url(r'^admin/', include(admin.site.urls)),
)

