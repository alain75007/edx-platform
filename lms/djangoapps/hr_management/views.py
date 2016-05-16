import logging

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, Http404

from django.views.generic.base import TemplateView

from microsite_configuration import microsite
from microsite_configuration.models import Microsite
from xmodule.modulestore.django import modulestore

from organizations.models import Organization

log = logging.getLogger(__name__)

@login_required
def index(request):
    user = request.user
    domain = request.META.get('HTTP_HOST', None)
    microsite = Microsite.get_microsite_for_domain(domain)
    organization = microsite.get_organizations()

    context = {
        'message': 'hr index',
        'user': user,
        'microsite': microsite,
        'organization': organization
    }
    return render(request, 'hr_management/index.html',context)

@login_required
def user_list(request):
    #get all users belonging to specific Org
    user = request.user
    domain = request.META.get('HTTP_HOST', None)
    microsite = Microsite.get_microsite_for_domain(domain)
    organization = microsite.get_organizations()
    organization = organization[0]

    users = Organization.objects.get(short_name=organization).users.all()

    context = {
        'message': 'hr user list',
        'user': user,
        'microsite': microsite,
        'organization': organization,
        'users': users
    }
    return render(request, 'hr_management/users.html',context)

@login_required
def course_list(request):
    user = request.user
    domain = request.META.get('HTTP_HOST', None)
    microsite = Microsite.get_microsite_for_domain(domain)
    organization = microsite.get_organizations()
    organization = organization[0]

    courses = [c for c in modulestore().get_courses() if c.org == organization]

    context = {
        'message': 'hr course list',
        'user': user,
        'microsite': microsite,
        'organization': organization,
        'courses': courses
    }
    return render(request, 'hr_management/courses.html',context)

