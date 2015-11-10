from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TLRweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    # testing templates
    url(r'^$', 'TLRweb.views.home', name='home'),
    
    url(r'^admin/', include(admin.site.urls)),
)