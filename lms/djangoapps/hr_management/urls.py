from django.conf import settings
from django.conf.urls import include, patterns, url

from hr_management import views

urlpatterns = patterns(
    '',
    url(r'^$',views.index.as_view(), name='index'),
    url(r'^users$',views.user_list.as_view(), name='user_list'),
    url(r'^courses$',views.course_list.as_view(), name='course_list'),
)