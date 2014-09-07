# -*- coding: utf-8 -*-

from django.conf.urls import url, patterns
from apps.doc.views.panel.admin.Country import CountryListView, CountryCreateView, \
    CountryUpdateView, CountryDeleteView


urlpatterns = patterns('',

                       #Country Urls
                       url(r'^list/$',
                           CountryListView.as_view(),
                           name='country_list'),
                       url(r'^create/$',
                           CountryCreateView.as_view(),
                           name='country_create'),
                       url(r'^edit/(?P<pk>\d+)/$',
                           CountryUpdateView.as_view(),
                           name='country_edit'),
                       url(r'^delete/(?P<pk>\d+)/$',
                           CountryDeleteView.as_view(),
                           name='country_delete')
                       )