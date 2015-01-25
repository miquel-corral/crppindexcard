# from __future__ import unicode_literals

import csv
import sys
import os

from django.conf import settings

project_path = "/Users/miquel/UN/0003-CRPTDEV/crppindexcard/"
sys.path.append(project_path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'crppindexcard.settings'

# OBS: to initialize Django in 1.7 and run python scripts. Do not include 'setup' in installed_apps
import django
django.setup()

from django.contrib.auth.models import User
from crppindexcard.models import IndexCard, Section, QuestionShort, QuestionLong

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
                    if (type == 'L'):
                        question = QuestionLong()
                    else:
                        question = QuestionShort()
                    question.code = code
                    question.statement = statement
                    question.comments = remarks
                    question.section = section
                    question.index_card = index_card
                    try:
                        question.save()
                    except:
                        print("Saving questions: " + question.name)
                        print("Unexpected error:", sys.exc_info())
    print("load_questions_file. End....")

if __name__ == "__main__":
    load_cities_file()
    load_sections_file()
    load_questions_file()
