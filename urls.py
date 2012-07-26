from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^post_app/$', 'post_app.views.index', name="index"),
    url(r'^post_app/home$', 'post_app.views.home',name="home"),
    url(r'^post_app/login$', 'post_app.views.login',name="login"),
    url(r'^post_app/viewpost$', 'post_app.views.viewpost',name="viewpost"),
    url(r'^post_app/comment/(?P<post>\d+)/$', 'post_app.views.comment',name="comment"),
    #url(r'^post_app/comment$', 'post_app.views.comment',name="comment"),
    url(r'^post_app/addpost$', 'post_app.views.addpost',name="addpost"),
    url(r'^post_app/logout$','post_app.views.logout_view',name="logout"),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    )