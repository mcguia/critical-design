import django
from django.contrib.auth import views as auth_views

if django.VERSION[:2] < (1, 8):
    from django.conf.urls import patterns, include, url
else:
    from django.conf.urls import include, url

from django.contrib import admin

from django_comments_xtd import LatestCommentFeed

from simple_threads import views
from simple_threads import forms

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


admin.autodiscover()


pattern_list = [
    url(r'^$', views.homepage, name='homepage'),
	# url(r'^profile/^(?P<profile_id>[0-9]+)/$', views.profile, name='profile'),
    url(r'^profile/comments/', views.user_comments, name='user-comments'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^articles/', include('simple_threads.articles.urls'), name='articles'),
    url(r'^comments/', include('django_comments_xtd.urls')),

    url(r'^feeds/comments/$', LatestCommentFeed(), name='comments-feed'),    
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),

     url(r'^register/$', views.register_user, name = 'register'),
]

urlpatterns = None

if django.VERSION[:2] < (1, 8):
    urlpatterns = patterns('views', *pattern_list)
else:
    urlpatterns = pattern_list


