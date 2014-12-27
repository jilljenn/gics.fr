from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from gics.views import MarkdownView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gics.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'gics.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^page/(?P<slug>[\w/-]+)/$', MarkdownView.as_view()),
) #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
