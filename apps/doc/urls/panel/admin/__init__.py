from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^country/', include('apps.doc.urls.panel.admin.country')),
)