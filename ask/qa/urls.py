from django.conf.urls import patterns, include, url

urlpatterns = patterns('', 
    url(r'^login/$', 'qa.views.login', name='login'),
    url(r'^signup/$', 'qa.views.signup', name='signup'),
    url(r'^question/\w+/$', 'qa.views.question', name='question'),
    url(r'^ask/$', 'qa.views.ask', name='ask'),
    url(r'^popular/$', 'qa.views.popular', name='popular'),
    url(r'^new/$', 'qa.views.new', name='new'),
    url(r'^$', 'qa.views.home', name='home'),
)
