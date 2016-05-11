import logging

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, Http404

from django.views.generic.base import TemplateView

log = logging.getLogger(__name__)

@login_required
def index(request):
    user = request.user
    microsite = '' #need to grab from request object

    context = {
        'message': 'hr index',
        'user': user,
        'microsite': microsite
    }
    return render(request, 'hr_management/index.html',context)


def user_list(request):
    #get all users belonging to specific Org
    context = {
        'message': 'hr user list',
    }
    return render(request, 'hr_management/index.html',context)

def course_list(request):
    #get all courses belonging to NYIF???
    #view here will allow courses to be copied into hr_manager's microsite Org
    context = {
        'message': 'hr course lits'
    }
    return render(request, 'hr_management/index.html',context)
