import logging

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, Http404

from django.views.generic.base import TemplateView

from microsite_configuration import microsite
from microsite_configuration.models import Microsite

#TODO figure out if we want to make this code dependent on edx-organizations
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
    #not sure what to do here:
    #   1. get all courses belonging to NYIF??? 
    #       - allow hr-manager to add courses to their catalog
    #   2, get all courses associated with Org
    #       - needs to be pre approved by NYIF staff
    #view here will allow courses to be copied into hr_manager's microsite Org
    user = request.user
    domain = request.META.get('HTTP_HOST', None)
    microsite = Microsite.get_microsite_for_domain(domain)
    organization = microsite.get_organizations()


    # microsite_org = microsite.get_value('course_org_filter')
    courses = ''

    context = {
        'message': 'hr course list',
        'user': user,
        'microsite': microsite,
        'organization': organization,
        'courses': courses
    }
    return render(request, 'hr_management/courses.html',context)

