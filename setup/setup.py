# from __future__ import unicode_literals

import csv
import sys
import os

from django.conf import settings

project_path = "/Users/miquel/UN/0003-CRPTDEV/crppindexcard/"
sys.path.append(project_path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'crppindexcard.settings'

from crppindexcard.constants import *


# OBS: to initialize Django in 1.7 and run python scripts. Do not include 'setup' in installed_apps
import django
django.setup()

from django.contrib.auth.models import User
from crppindexcard.models import IndexCard, Section, Question, Hazard, HazardCategory, HazardAssessmentMatrix, Service,\
    ServiceComponent, ServiceT1Question, ServiceT2Question, ServiceT3Question, IndexCardService, ServiceT5Question, \
     CompetenceQuestion

import crppindexcard.constants

def load_users_file():
    """
    Load into database users for cities in users.csv file
    :return:
    """
    print("load_users_file. Start..")
    file_path = settings.BASE_DIR + "/files/users.csv"
    data_reader = csv.reader(open(file_path), delimiter=",", quotechar='"')
    for row in data_reader:
        # read data from line
        username = row[0].strip()
        pwd = row[1].strip()
        try:
            user = User.objects.create_user(username, 'test@test.com', pwd)
            user.first_name = username
            user.save()
        except:
            print("Saving user: " + row[1].strip())
            print("Unexpected error:", sys.exc_info())
    print("load_users_file. End....")


def load_cities_file():
    """
    Load into database contents from cities.csv file
    :return:
    """
    print("load_cities_file. Start..")
    file_path = settings.BASE_DIR + "/files/cities.csv"
    data_reader = csv.reader(open(file_path), delimiter=",", quotechar='"')
    for row in data_reader:
        # read data from line
        code = row[0].strip()
        name = row[1].strip()
        user = row[2].strip()
        # create index card entry
        index_card = IndexCard()
        index_card.city = name
        index_card.name = code + "-" + name
        index_card.code = code
        index_card.username = user
        try:
            index_card.save()
        except:
            print("Saving index_card: " + row[1].strip())
            print("Unexpected error:", sys.exc_info())
    print("load_cities_file. End....")

def load_sections_file():
    """
    Load into database contents from sections.csv file
    :return:
    """
    print("load_sections_file. Start..")
    file_path = settings.BASE_DIR + "/files/sections.csv"
    for index_card in IndexCard.objects.all():
        data_reader = csv.reader(open(file_path), delimiter=",", quotechar='"')
        for row in data_reader:
            # read data from line
            code = row[0].strip()
            name = row[1].strip()
            # create section entry
            section = Section()
            section.name = name
            section.code = code
            section.index_card = index_card
            try:
                section.save()
            except:
                print("Saving sections: " + row[1].strip())
                print("Unexpected error:", sys.exc_info())
    print("load_sections_file. End....")

def load_questions_file():
    """
    Load into database questions from questions.tsv file
    :return:
    """
    print("load_questions_file. Start..")
    file_path = settings.BASE_DIR + "/files/questions.tsv"
    data_reader = csv.reader(open(file_path), dialect='excel-tab')
    for row in data_reader:
        # read data from line
        section_code = row[0].strip()
        code = row[1].strip()
        type = row[2].strip()
        statement = row[3].strip()
        remarks = row[4].strip()
        # add question to each proper section for all index_cards
        for index_card in IndexCard.objects.all():
            for section in index_card.section_set.all():
                if section.code == section_code:
                    # new question
                    question = Question()
                    question.answer_type = type
                    question.code = code
                    question.statement = statement
                    question.comments = remarks
                    question.section = section
                    question.index_card = index_card
                    try:
                        question.save()
                    except:
                        print("Saving questions: " + question.code)
                        print("Unexpected error:", sys.exc_info())
    print("load_questions_file. End....")


def load_hazards_file():
    print("load_hazards_file. Start....")
    file_path = settings.BASE_DIR + "/files/hazards.csv"
    data_reader = csv.reader(open(file_path), delimiter=",", quotechar='"')
    for row in data_reader:
        hazard_name = row[0].strip()
        hazard_category_name = row[1].strip()
        # search for hazard category
        try:
            hazard_category = HazardCategory.objects.get(name=hazard_category_name)
        except:
            hazard_category = HazardCategory()
            hazard_category.name = hazard_category_name
            hazard_category.save()
        # create hazard
        hazard = Hazard()
        hazard.name = hazard_name
        hazard.category = hazard_category
        hazard.save()
    print("load_hazards_file. End....")


def load_services_file():
    print("load_services_file. Start....")
    file_path = settings.BASE_DIR + "/files/services.csv"
    data_reader = csv.reader(open(file_path), delimiter=",", quotechar='"')
    for row in data_reader:
        service_name = row[0].strip()
        service_component_name = row[1].strip()
        # search service
        try:
            service = Service.objects.get(name=service_name)
        except:
            service = Service()
            service.name = service_name
            service.save()
        # add service component
        service_component = ServiceComponent()
        service_component.name = service_component_name
        service_component.service = service
        service_component.save()
        print("Added service_component: " + service_component_name + " to service: " + service_name)

    print("load_services_file. End....")


def generate_hazard_questions_no_services():
    print("generate_hazard_questions_no_services. Start....")
    # for each index card assign hazards
    for index_card in IndexCard.objects.all():
        print("index_card.username:" + index_card.username)
        for hazard in Hazard.objects.all():
            print("hazard.name: " + hazard.name)
            if hazard.name.find('Services') == -1:
                hazard_matrix = HazardAssessmentMatrix()
                hazard_matrix.hazard = hazard
                hazard.save()
            index_card.hazards.add(hazard)
        index_card.save()
    print("generate_hazard_questions_no_services. End....")


def generate_services_list():
    print("generate_services_list. Start....")
    for index_card in IndexCard.objects.all():
        print("index_card.username:" + index_card.username)
        for service in Service.objects.all():
            print("service.name: " + service.name)
            index_card_service = IndexCardService()
            index_card_service.service = service
            index_card_service.index_card = index_card
            index_card_service.save()
    print("generate_services_list. End....")


def generate_services_questions():
    print("generate_services_questions. Start....")
    for index_card in IndexCard.objects.all():
        for index_card_service in index_card.indexcardservice_set.all():
            service_question = None
            print("service.name: " + index_card_service.service.name)
            service_component_list = list(index_card_service.service.servicecomponent_set.all())
            service_component_list_count = len(service_component_list)
            if service_component_list_count == 1:
                service_question = ServiceT1Question()
                service_question.component_1_label = service_component_list[0].name
            if service_component_list_count == 2:
                service_question = ServiceT2Question()
                service_question.component_1_label = service_component_list[0].name
                service_question.component_2_label = service_component_list[1].name
            if service_component_list_count == 3:
                service_question = ServiceT3Question()
                service_question.component_1_label = service_component_list[0].name
                service_question.component_2_label = service_component_list[1].name
                service_question.component_3_label = service_component_list[2].name
            if  service_component_list_count == 5:
                service_question = ServiceT5Question()
                service_question.component_1_label = service_component_list[0].name
                service_question.component_2_label = service_component_list[1].name
                service_question.component_3_label = service_component_list[2].name
                service_question.component_4_label = service_component_list[3].name
                service_question.component_5_label = service_component_list[4].name

            service_question.index_card_service = index_card_service
            service_question.save()

    print("generate_services_questions. End....")


def generate_infrastructure_questions():
    print("generate_infrastructure_questions. Start....")
    for index_card in IndexCard.objects.all():
        for index_card_service in index_card.indexcardservice_set.all():
            for service_component in index_card_service.service.servicecomponent_set.all():
                competence_question = CompetenceQuestion()
                question_name = index_card_service.service.name
                if question_name != service_component.name:
                    question_name = question_name + " - " + service_component.name
                competence_question.label_text = question_name
                print("competence_question.label_text: " + competence_question.label_text)
                competence_question.index_card = index_card
                competence_question.save()

    print("generate_infrastructure_questions. End....")


def test():
    print("test. Start....")
    for index_card in IndexCard.objects.all():
        for index_card_service in index_card.indexcardservice_set.all():
            print("index_card: " + index_card.username + " - service.name: " + index_card_service.service.name)
            #for service_component in index_card_service.service.servicecomponent_set.all():
            #    print("service_component: " + service_component.name)

            service_components_list = list(index_card_service.service.servicecomponent_set.all())
            if(len(service_components_list)==1):
                print("component 0:" + service_components_list[0].name)
            if(len(service_components_list)==2):
                print("component 0:" + service_components_list[0].name)
                print("component 1:" + service_components_list[1].name)
            if(len(service_components_list)==3):
                print("component 0:" + service_components_list[0].name)
                print("component 1:" + service_components_list[1].name)
                print("component 2:" + service_components_list[2].name)
            if(len(service_components_list)==5):
                print("component 0:" + service_components_list[0].name)
                print("component 1:" + service_components_list[1].name)
                print("component 2:" + service_components_list[2].name)
                print("component 3:" + service_components_list[3].name)
                print("component 4:" + service_components_list[4].name)
    print("test. End....")



if __name__ == "__main__":

    load_users_file()
    load_cities_file()
    load_sections_file()
    load_questions_file()
    load_hazards_file()
    generate_hazard_questions_no_services()
    load_services_file()
    generate_services_list()
    generate_services_questions()
    generate_infrastructure_questions()
    #load_hard_infrastructure_file()
    #generate_hard_infrastructure_questions()
    #load_built_infrastructure_file()
    #generate_built_infrastructure_questions()
    #load_built_environment_file()
    #generate_built_environment_questions()
    #load_environment_file()
    #generate_environment_questions()
    #test()

