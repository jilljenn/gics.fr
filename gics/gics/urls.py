from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from gics.views import MarkdownView, SchoolList, SessionList, SchoolDetail, LectureList, LectureDetail, NewsList, NewsDetail, QuestionList, DisciplineDetail
from wiki.urls import get_pattern as get_wiki_pattern
from django_nyt.urls import get_pattern as get_nyt_pattern

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gics.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'gics.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^page/(?P<slug>[\w/-]+)/$', MarkdownView.as_view()),
    url(r'^page/(?P<slug>[\w/-]+)/$', MarkdownView.as_view()),
    url(r'^lycees/$', SchoolList.as_view(), name='school-list'),
    url(r'^lycees/(?P<pk>\d+)$', SchoolDetail.as_view(), name='school-detail'),
    url(r'^ateliers/$', LectureList.as_view()),
    url(r'^ateliers/(?P<pk>\d+)$', LectureDetail.as_view()),
    url(r'^ateliers/(?P<slug>\w+)/$', DisciplineDetail.as_view()),
    url(r'^news/$', NewsList.as_view()),
    url(r'^news/(?P<pk>\d+)$', NewsDetail.as_view()),
    url(r'^contact/$', 'gics.views.contact'),
    url(r'^register/$', 'gics.views.register'),
    url(r'^faq/$', QuestionList.as_view()),
    url(r'^forum/$', 'gics.views.forum'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^notifications/', get_nyt_pattern()),
    url(r'^wiki/', get_wiki_pattern()),
    url(r'^(?P<slug>[\w-]+)/$', 'gics.views.follow_alias'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
