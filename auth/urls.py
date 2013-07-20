from django.conf.urls import patterns, include, url

urlpatterns = patterns('auth',
    url('^login/$', 'views.login', name='login'),
    url('^logout/$', 'views.logout', name='logout'),
    url('^signup/$', 'views.signup', name='signup'),
)
