import logging

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, Http404

from django.views.generic.base import TemplateView

from microsite_configuration.models import Microsite


log = logging.getLogger(__name__)

@login_required
def index(request):
    user = request.user
    domain = request.META.get('HTTP_HOST', None)
    microsite = Microsite.get_microsite_for_domain(domain)
    organization = '' #microsite.get_organizations()

    context = {
        'message': 'hr index',
        'user': user,
        'microsite': microsite,
        'organization': organization
    }
    return render(request, 'hr_management/index.html',context)


def user_list(request):
    #get all users belonging to specific Org
    user = request.user
    domain = request.META.get('HTTP_HOST', None)
    microsite = Microsite.get_microsite_for_domain(domain)
    organization = '' #microsite.get_organizations()

    # users = User.object.filter()

    context = {
        'message': 'hr user list',
        'user': user,
        'microsite': microsite,
        'organization': organization,
        'users': users
    }
    return render(request, 'hr_management/users.html',context)


def course_list(request):
    #get all courses belonging to NYIF???
    #view here will allow courses to be copied into hr_manager's microsite Org
    user = request.user
    domain = request.META.get('HTTP_HOST', None)
    microsite = Microsite.get_microsite_for_domain(domain)
    organization = '' #microsite.get_organizations()

    courses = ''

    context = {
        'message': 'hr course list',
        'user': user,
        'microsite': microsite,
        'organization': organization,
        'courses': courses
    }
    return render(request, 'hr_management/courses.html',context)

