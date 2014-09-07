from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    #Website
    url(r'^', include('apps.doc.urls.website')),

    #Panel
    url(r'^panel/', include('apps.doc.urls.panel')),

    #social
    url('', include('social.apps.django_app.urls', namespace='social'))
)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': settings.MEDIA_ROOT}))