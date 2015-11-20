from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'',include('photo.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login_url'),
    url(r'^accounts/signup/$', 'photo.views.signup', name='signup'),
    url(r'^accounts/signup_ok/$', TemplateView.as_view(template_name='registration/signup_ok.html'), name='signup_ok'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout_url'),

)

