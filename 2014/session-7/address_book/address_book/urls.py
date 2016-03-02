from django.conf.urls import patterns, include, url
from django.contrib import admin
from contacts.views import IndexView, AboutView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^secret/', include(admin.site.urls)),
    url(r'^Aboutus', AboutView.as_view())
)
