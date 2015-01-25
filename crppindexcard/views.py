# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.template.response import TemplateResponse
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.decorators import login_required

from crppindexcard.models import IndexCard


def my_login(request):
    username = ''
    password = ''
    user = None

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login_response = login(request, user)
                    try:
                        index_card = IndexCard.objects.get(username=request.user)
                    except:
                        index_card = None
                    template = loader.get_template('crppindexcard/index.html')
                    context = RequestContext(request, {
                        'index_card': index_card,
                        'user': user,
                    })
                    return HttpResponse(template.render(context))
                else:
                    # Return a 'disabled account' error message
                    context = {'form': form}
                    return redirect('/login/?next=%s' % request.path)
            else:
                # Return an 'invalid login' error message.
                context = {'form': form}
                return TemplateResponse(request, 'crppindexcard/login.html', context)
        else:
            context = {'form': form}
            return TemplateResponse(request, 'crppindexcard/login.html', context)
    else:
        form = AuthenticationForm(request)
#        current_site = None
        context = {'form': form,
#           'site': current_site,
#            'site_name': current_site.name,
            }
        return TemplateResponse(request, 'crppindexcard/login.html', context)




def my_logout(request):
    logout(request)
    template = loader.get_template('crppindexcard/logout.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


@login_required
def index(request):
    """
    View for the assessment list
    TODO: filter by user/city

    :param request:
    :return:
    """

    #assessments = Assessment.objects.all()
    #ra_sections = RiskAssessmentSection.objects.all()
    #ca_sections = CapacityAssessmentSection.objects.all()
    template = loader.get_template('crppindexcard/index.html')
    context = RequestContext(request, {
        'city': 'test_city',
    })
    return HttpResponse(template.render(context))
