# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import redirect, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.template.response import TemplateResponse
from django.contrib.auth.forms import AuthenticationForm
from django.forms.models import modelformset_factory
from django import forms

from django.contrib.auth.decorators import login_required

from crppindexcard.models import IndexCard, Question, Hazard, HazardAssessmentMatrix, ServiceT1Question, \
    ServiceT2Question, ServiceT3Question, ServiceT5Question

import crppindexcard.constants

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
                    request.session['username'] = username
                    return redirect('/index/')
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
    View for the list of sections of the index card

    :param request:
    :return:
    """
    username = request.session.get('username')
    try:
        index_card = IndexCard.objects.get(username=username)
    except:
        index_card = None
    template = loader.get_template('crppindexcard/index.html')
    context = RequestContext(request, {
        'index_card': index_card,
        'username': username,
    })
    return HttpResponse(template.render(context))


@login_required
def section_questions(request, index_card_id, section_id):
    """
    View for the questions of a specified index card and section

    :param request:
    :return:
    """
    fields_to_show = \
        ('statement','answer_type', 'answer_short', 'answer_long', 'comments')
    read_only_fields = ('comments')
    QuestionFormSet = modelformset_factory(Question, max_num=1)
    index_card = IndexCard.objects.get(id=index_card_id)
    section = index_card.section_set.get(id = section_id)

    if request.method == 'POST':
        formset = QuestionFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return render_to_response("crppindexcard/index.html",
                                      {'index_card': index_card})
        else:
            if format(len(formset.errors) > 0):
                num_errors = len(formset.errors[0])
        set_form_hidden_fields(formset, fields_to_show)
        set_form_readonly_fields(formset, read_only_fields)
    else:
        query_set = Question.objects.filter(section_id = section_id).order_by('id')
        formset = QuestionFormSet(queryset = query_set)
        set_form_readonly_fields(formset, read_only_fields)
        set_form_hidden_fields(formset, fields_to_show)

    return render_to_response("crppindexcard/section_questions.html", {
    "formset": formset,
    "index_card": index_card,
    "section": section,
    }, context_instance=RequestContext(request))


@login_required
def hazard_questions(request, index_card_id, hazard_id):
    """
    View for the questions of a specified index card and hazard

    :param request:
    :return:
    """
    #fields_to_show = \
    #    ('statement','answer_type', 'answer_short', 'answer_long', 'comments')
    #read_only_fields = ('comments')


    QuestionFormSet = modelformset_factory(HazardAssessmentMatrix, max_num=1)
    index_card = IndexCard.objects.get(id=index_card_id)
    hazard = index_card.hazards.get(id = hazard_id)

    if request.method == 'POST':
        formset = QuestionFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return render_to_response("crppindexcard/index.html",
                                      {'index_card': index_card})
        else:
            if format(len(formset.errors) > 0):
                num_errors = len(formset.errors[0])
        #set_form_hidden_fields(formset, fields_to_show)
        #set_form_readonly_fields(formset, read_only_fields)
    else:
        query_set = hazard.hazardassessmentmatrix_set.all().order_by('id')
        formset = QuestionFormSet(queryset = query_set)
        #set_form_readonly_fields(formset, read_only_fields)
        #set_form_hidden_fields(formset, fields_to_show)

    return render_to_response("crppindexcard/hazard_questions.html",
                              dict(formset=formset, index_card=index_card, hazard=hazard, constants=crppindexcard.constants), \
                              context_instance=RequestContext(request))

@login_required
def services_list(request, index_card_id, hazard_id):
    """
    View for the list of services of an index card

    :param request:
    :return:
    """
    try:
        index_card = IndexCard.objects.get(id=index_card_id)
        hazard = index_card.hazards.get(id = hazard_id)
    except:
        index_card = None
        hazard = None
    template = loader.get_template('crppindexcard/services_list.html')
    context = RequestContext(request, {
        'index_card': index_card,
        'hazard': hazard,
    })
    return HttpResponse(template.render(context))


@login_required
def service_questions(request, index_card_id, hazard_id, index_card_service_id):
    """
    View for the questions of a specified index card and hazard

    :param request:
    :return:
    """
    #fields_to_show = \
    #    ('statement','answer_type', 'answer_short', 'answer_long', 'comments')
    #read_only_fields = ('comments')

    index_card = IndexCard.objects.get(id=index_card_id)
    index_card_service = index_card.indexcardservice_set.get(id=index_card_service_id)
    hazard = Hazard.objects.get(id=hazard_id)
    service_component_list = index_card_service.service.servicecomponent_set.all()
    service_component_list_count = len(service_component_list)

    if service_component_list_count == 1:
        QuestionFormSet = modelformset_factory(ServiceT1Question, max_num=1)
    if service_component_list_count == 2:
        QuestionFormSet = modelformset_factory(ServiceT2Question, max_num=1)
    if service_component_list_count == 3:
        QuestionFormSet = modelformset_factory(ServiceT3Question, max_num=1)
    if service_component_list_count == 5:
        QuestionFormSet = modelformset_factory(ServiceT5Question, max_num=1)

    if request.method == 'POST':
        formset = QuestionFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return render_to_response("crppindexcard/services_list.html",
                                      {'index_card': index_card,
                                       'hazard': hazard})
        else:
            if format(len(formset.errors) > 0):
                num_errors = len(formset.errors[0])
        #set_form_hidden_fields(formset, fields_to_show)
        #set_form_readonly_fields(formset, read_only_fields)
    else:
        if service_component_list_count == 1:
            query_set = ServiceT1Question.objects.filter(index_card_service_id=index_card_service_id)
            template_name = "crppindexcard/service_t1_questions.html"

            #formset = QuestionFormSet(queryset = query_set)
            #return render_to_response("crppindexcard/service_t1_questions.html",
            #    dict(formset=formset, index_card=index_card, hazard=hazard, service=index_card_service.service, \
            #    constants=crppindexcard.constants), context_instance=RequestContext(request))

        if service_component_list_count == 2:
            query_set = ServiceT2Question.objects.filter(index_card_service_id=index_card_service_id)
            template_name = "crppindexcard/service_t2_questions.html"

        if service_component_list_count == 3:
            query_set = ServiceT3Question.objects.filter(index_card_service_id=index_card_service_id)
            template_name = "crppindexcard/service_t3_questions.html"

        if service_component_list_count == 5:
            query_set = ServiceT5Question.objects.filter(index_card_service_id=index_card_service_id)
            template_name = "crppindexcard/service_t5_questions.html"

        formset = QuestionFormSet(queryset=query_set)
        return render_to_response(template_name,
                dict(formset=formset, index_card=index_card, hazard=hazard, service=index_card_service.service, \
                constants=crppindexcard.constants), context_instance=RequestContext(request))


### OBS: cal enviar resposta a tres templates diferents!!!!!!!

        #formset = QuestionFormSet(queryset = query_set)
        #set_form_readonly_fields(formset, read_only_fields)
        #set_form_hidden_fields(formset, fields_to_show)
"""
    return render_to_response("crppindexcard/service_questions.html",
                              dict(formset=formset, index_card=index_card, hazard=hazard), \
                              context_instance=RequestContext(request))
"""

def set_form_hidden_fields(formset, fields_to_show):
    """
    Function to set hidden fields and show fields of each form in formset
    :param formset:
    :param files_to_show:
    :return:
    """
    for form in formset:
        for field in form.fields:
            if not any(field in s for s in fields_to_show):
                form.fields[field].widget = forms.HiddenInput()

def set_form_readonly_fields(formset, read_only_fields):
    """
    Function to set readonly fields of each form in formset
    :param formset:
    :return:
    """
    for form in formset:
        for field in form.fields:
            print(field)
            if any(field in s for s in read_only_fields):
                print(field)
                form.fields[field].widget.attrs['disabled'] = True