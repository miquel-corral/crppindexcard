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
    CompetenceQuestion, CompetenceComponent, CompetenceCategory, IndexCardCompetenceCategory, Ownership, Competence, \
    RoleInECPlans, Operator, Dimension, Component, System, Element, ResilienceCharacteristic, ResiliencePrinciple, \
    ElementQuestionCharField, ServiceT4Question


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
        for index_card in IndexCard.objects.all().order_by('id'):
            for section in index_card.section_set.all().order_by('id'):
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


def load_organizational_file():
    print("load_organizational_file. Start....")
    file_path = settings.BASE_DIR + "/files/organizational.csv"
    data_reader = csv.reader(open(file_path), delimiter=",", quotechar='"')
    for row in data_reader:
        competence_category_name = row[0].strip()
        competence_component_name = row[1].strip()
        # search service
        try:
            competence_category = CompetenceCategory.objects.get(name=competence_category_name)
        except:
            competence_category = CompetenceCategory()
            competence_category.name = competence_category_name
            competence_category.save()
        # add service component
        competence_component = CompetenceComponent()
        competence_component.name = competence_component_name
        competence_component.competence_category = competence_category
        competence_component.save()
        print("Added competence_component: " + competence_component.name + " to competence_category: " + competence_category.name)

    print("load_organizational_file. End....")

def generate_hazard_questions_no_services():
    print("generate_hazard_questions_no_services. Start....")
    # for each index card assign hazards
    for index_card in IndexCard.objects.all().order_by('id'):
        print("index_card.username:" + index_card.username)
        for hazard in Hazard.objects.all().order_by('id'):
            print("hazard.name: " + hazard.name)
            if hazard.name.find('Services') == -1:
                hazard_matrix = HazardAssessmentMatrix()
                hazard_matrix.hazard = hazard
                hazard_matrix.index_card = index_card
                hazard_matrix.save()
            index_card.hazards.add(hazard)
        index_card.save()
    print("generate_hazard_questions_no_services. End....")


def generate_services_list():
    print("generate_services_list. Start....")
    for index_card in IndexCard.objects.all().order_by('id'):
        print("index_card.username:" + index_card.username)
        for service in Service.objects.all().order_by('id'):
            print("service.name: " + service.name)
            index_card_service = IndexCardService()
            index_card_service.service = service
            index_card_service.index_card = index_card
            index_card_service.save()
    print("generate_services_list. End....")


def generate_services_questions():
    print("generate_services_questions. Start....")
    for index_card in IndexCard.objects.all():
        for index_card_service in index_card.indexcardservice_set.all().order_by('id'):
            service_question = None
            print("service.name: " + index_card_service.service.name)
            service_component_list = list(index_card_service.service.servicecomponent_set.all().order_by('id'))
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
            if  service_component_list_count == 4:
                service_question = ServiceT4Question()
                service_question.component_1_label = service_component_list[0].name
                service_question.component_2_label = service_component_list[1].name
                service_question.component_3_label = service_component_list[2].name
                service_question.component_4_label = service_component_list[3].name
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


def generate_organizational_components_list():
    print("generate_organizational_components_list. Start....")
    for index_card in IndexCard.objects.all():
        print("index_card.username:" + index_card.username)
        for competence_category in CompetenceCategory.objects.all().order_by('id'):
            print("competence_category.name: " + competence_category.name)
            index_card_competence_category = IndexCardCompetenceCategory()
            index_card_competence_category.competence_category = competence_category
            index_card_competence_category.index_card = index_card
            index_card_competence_category.save()
    print("generate_organizational_components_list. End....")


def generate_organizational_questions():
    print("generate_infrastructure_questions. Start....")
    for index_card in IndexCard.objects.all():
        for index_card_competence_category in index_card.indexcardcompetencecategory_set.all().order_by('id'):
            for competence_component in CompetenceComponent.objects.filter(competence_category=index_card_competence_category.competence_category):
                competence_question = CompetenceQuestion()
                competence_question.label_text = competence_component.name
                print("competence_question.label_text: " + competence_question.label_text)
                competence_question.index_card_competence_category = index_card_competence_category
                competence_question.save()

    print("generate_infrastructure_questions. End....")


def load_file_one_field_entity(file_name, class_name):
    print("load_file_one_field_entity. Start....")
    file_path = settings.BASE_DIR + "/files/" + file_name
    data_reader = csv.reader(open(file_path), delimiter=",", quotechar='"')
    for row in data_reader:
        field_name = row[0].strip()
        class_instance = class_name()
        class_instance.code = field_name
        class_instance.save()
    print("load_file_one_field_entity. End....")


def load_file_dimension_component():
    print("load_file_dimension_component. Start....")
    file_path = settings.BASE_DIR + "/files/" + "dimension_component.csv"
    data_reader = csv.reader(open(file_path), delimiter=",", quotechar='"')
    for row in data_reader:
        dimension_name = row[0].strip()
        component_name = row[1].strip()
        print("Dimension-component line: " + dimension_name + " - " + component_name)
        # only creates dimension if it is new
        try:
            dimension = Dimension.objects.get(code=dimension_name)
        except:
            dimension = Dimension()
            dimension.code = dimension_name
            dimension.save()
        # only creates component if it is new
        try:
            component = Component.objects.get(code=component_name)
        except:
            component = Component()
            component.code = component_name
            component.dimension = dimension
            component.save()
    print("load_file_dimension_component. End....")


def load_file_component_system_element():
    print("load_file_dimension_component. Start....")
    file_path = settings.BASE_DIR + "/files/" + "component_system_element.csv"
    data_reader = csv.reader(open(file_path), delimiter=",", quotechar='"')
    for row in data_reader:
        component_name = row[0].strip()
        system_name = row[1].strip()
        element_name = row[2].strip()
        # look for component (must exist)
        component = Component.objects.get(code=component_name)
        try:
            system = System.objects.get(code=system_name)
        except:
            system = System()
            system.code = system_name
            system.save()
            print("Adding component: " + component.code + " to system: " + system_name)
            system.components.add(component)
            system.save()
        try:
            print("Searching element: " + element_name + ", " +  "component: " + component.code + " to system: " + system.code)
            element = Element.objects.get(code=element_name,system=system,components=component)
        except:
            element = Element()
            element.code = element_name
            element.system = system
            element.save()
            element.components.add(component)
            element.save()
    print("load_file_dimension_component. End....")


def load_file_resilience_principles():
    print("load_file_resilience_principles. Start....")
    file_path = settings.BASE_DIR + "/files/" + "resilience_principles.csv"
    data_reader = csv.reader(open(file_path), delimiter=",", quotechar='"')
    for row in data_reader:
        characteristic_name = row[0].strip()
        principle_name = row[1].strip()
        try:
            characteristic = ResilienceCharacteristic.objects.get(code=characteristic_name)
        except:
            characteristic = ResilienceCharacteristic()
            characteristic.code = characteristic_name
            characteristic.save()
        try:
            principle = ResiliencePrinciple.objects.get(code=principle_name)
        except:
            principle = ResiliencePrinciple()
            principle.code = principle_name
            principle.resilience_characteristic = characteristic
            principle.save()

    print("load_file_resilience_principles. End....")


def load_file_component_elements_questions(file_name, component_name):
    print("load_file_physical_functional_question. Start....")
    file_path = settings.BASE_DIR + "/files/" + file_name
    for index_card in IndexCard.objects.all():
        for element in Element.objects.all():
            data_reader = csv.reader(open(file_path), dialect='excel-tab')
            print("element.name: " + element.code)
            #for component in element.components.all():
            #    print("component.code: " + component.code)
            print("numelements in Service Infrastructures: " + str(element.components.filter(code=component_name).count()))
            if (element.components.filter(code=component_name).count() > 0):
                if(element.elementquestioncharfield_set.count()==0):
                    print("element.name inside if: " + element.code)
                    for row in data_reader:
                        principle_name = row[0].strip()
                        question_code = row[1].strip()
                        question_statement = row[2].strip()
                        question_explanation = row[3].strip()
                        question_type = row[4].strip()
                        # principle, must exist
                        print("Processing row_: " + str(row))
                        print("Question type: " + str(question_type))
                        principle = ResiliencePrinciple.objects.get(code=principle_name)
                        # new question
                        element_question = ElementQuestionCharField(type=question_type)
                        #if question_type == ENGAGEMT_TYPE:
                        #    element_question.answer = CHOICES_ENGAGEMENT
                        #if question_type == YES_NO_TYPE:
                        #    element_question.answer = CHOICES_YES_NO
                        #if question_type == CHAR_TYPE:
                        #    element_question = ElementQuestionCharField()
                        #if question_type == INT_TYPE:
                        #    element_question = ElementQuestionInteger()
                        element_question.type = question_type
                        # save question. Will fail if not treatment type written
                        element_question.code = question_code
                        element_question.statement = question_statement
                        element_question.explanation = question_explanation
                        element_question.resilience_principle = principle
                        element_question.index_card = index_card
                        element_question.element = element
                        element_question.save()

    print("load_file_physical_functional_question. End....")

"""
def generate_element_questions():
    print("generate_element_questions. Start....")
    # for each element add question list of every type
    for element in Element.objects.all().order_by('id'):
        #for element_question in ElementQuestionInteger.objects.all().order_by('resilience_principle','code'):
        #    element_question.elements.add(element)
        for element_question in ElementQuestionCharField.objects.all().order_by('resilience_principle','code'):
            element_question.elements.add(element)
        #for element_question in ElementQuestionSelectYESNO.objects.all().order_by('resilience_principle','code'):
        #    element_question.elements.add(element)
        element_question.save()
    print("generate_element_questions. End....")
"""

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
    """
    load_users_file()
    load_cities_file()
    load_sections_file()
    load_questions_file()
    load_hazards_file()
    generate_hazard_questions_no_services()
    load_services_file()
    generate_services_list()
    generate_services_questions()
    load_organizational_file()
    generate_organizational_components_list()
    generate_organizational_questions()
    load_file_one_field_entity("ownership.csv", Ownership)
    load_file_one_field_entity("ownership.csv", Operator)
    load_file_one_field_entity("competences.csv", Competence)
    load_file_one_field_entity("roles_in_ec_plan.csv", RoleInECPlans)
    """
    load_file_dimension_component()
    load_file_component_system_element()
    #load_file_resilience_principles()
    load_file_component_elements_questions('service_supply_infrastructure_questions.tsv','Service Infrastructure')
    load_file_component_elements_questions('hard_infrastructure_questions.tsv','Hard Infrastructure')

    #test()

