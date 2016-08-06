from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as rest_views

from core import views

urlpatterns = [
    url(r'^users$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)$', views.UserDetail.as_view()),
    url(r'^tweets$', views.TweetList.as_view()),
    url(r'^tweets/(?P<pk>[0-9]+)$', views.TweetDetail.as_view()),
    url(r'^login', rest_views.obtain_auth_token)
]

urlpatterns = format_suffix_patterns(urlpatterns)
