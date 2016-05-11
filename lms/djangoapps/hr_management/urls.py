from django.conf import settings
from django.conf.urls import include, patterns, url

from hr_management import views

urlpatterns = patterns(
    'hr_management.views',
    url(r'^$','index', name='index'),
    url(r'^users$','user_list', name='user_list'),
    url(r'^courses$','course_list', name='course_list'),
)