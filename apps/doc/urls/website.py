from django.conf.urls import patterns, url
from apps.doc.views.website.home import HomeTemplateView,\
    LoginTemplateView, LoginUserView, LogoutView, ProfileTemplateView

urlpatterns = patterns('',
                       url(r'^$',
                           HomeTemplateView.as_view(),
                           name='home'),
                       url(r'^profile/$',
                           ProfileTemplateView.as_view(),
                           name='profile'),
                       url(r'^login/$',
                           LoginTemplateView.as_view(),
                           name='login'),
                       url(r'^login-user/$',
                           LoginUserView.as_view(),
                           name='login_user'),
                       url(r'^logout/$',
                           LogoutView.as_view(),
                           name='logout'),
)