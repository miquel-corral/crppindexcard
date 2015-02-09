# from django.db import models
import django.db.models
from django import forms
from constants import CHOICES_YES_NO, YES_NO_TYPE, CHOICES_ENGAGEMENT, ENGAGEMT_TYPE, CHAR_TYPE

class Common(django.db.models.Model):
    """
    Abstract class for common attributes and behaviour
    """
    code = django.db.models.CharField(max_length=100, unique=False)
    # ...

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.code

    class Meta:
        abstract = True


class HazardCategory(django.db.models.Model):
    """
    Represents a Hazard Category
    """
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

    name = django.db.models.CharField(max_length=250, null=False, blank=False)


class Hazard(django.db.models.Model):
    """
    Represents a single Hazard:
    """
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

    name = django.db.models.CharField(max_length=250, null=False, blank=False)
    category = django.db.models.ForeignKey(HazardCategory)

class Service(django.db.models.Model):
    """
    Represents a service
    """
    name = django.db.models.CharField(max_length=100, null=False, blank=False)


class ServiceComponent(django.db.models.Model):
    """
    Represents aservice component
    """
    name = django.db.models.CharField(max_length=100, null=False, blank=False)
    service = django.db.models.ForeignKey(Service)


class IndexCard(Common):
    """
    Represents Index Card Entry for a City to link index card with user
    """
    city = django.db.models.CharField(max_length=100, unique=True)
    username = django.db.models.CharField(max_length=100, unique=True)
    hazards = django.db.models.ManyToManyField(Hazard)

class HazardAssessmentMatrix(django.db.models.Model):
    """
    Represents matrix question for hazard assessment
    """
    events_past_or_expected = django.db.models.CharField(max_length=100, null=True, blank=True)
    it_no_losses = django.db.models.CharField(max_length=100, null=True, blank=True)
    it_disruption_function = django.db.models.CharField(max_length=100, null=True, blank=True)
    it_material_losses = django.db.models.CharField(max_length=100, null=True, blank=True)
    it_casualties = django.db.models.CharField(max_length=100, null=True, blank=True)
    st_no_losses = django.db.models.CharField(max_length=100, null=True, blank=True)
    st_disruption_function = django.db.models.CharField(max_length=100, null=True, blank=True)
    st_material_losses = django.db.models.CharField(max_length=100, null=True, blank=True)
    st_casualties = django.db.models.CharField(max_length=100, null=True, blank=True)
    mt_no_losses = django.db.models.CharField(max_length=100, null=True, blank=True)
    mt_disruption_function = django.db.models.CharField(max_length=100, null=True, blank=True)
    mt_material_losses = django.db.models.CharField(max_length=100, null=True, blank=True)
    mt_casualties = django.db.models.CharField(max_length=100, null=True, blank=True)
    lt_no_losses = django.db.models.CharField(max_length=100, null=True, blank=True)
    lt_disruption_function = django.db.models.CharField(max_length=100, null=True, blank=True)
    lt_material_losses = django.db.models.CharField(max_length=100, null=True, blank=True)
    lt_casualties = django.db.models.CharField(max_length=100, null=True, blank=True)
    mov = django.db.models.TextField(null=True, blank=True)
    additional_information = django.db.models.TextField(null=True, blank=True)
    hazard = django.db.models.ForeignKey(Hazard)
    index_card = django.db.models.ForeignKey(IndexCard)

class Section(Common):
    """
    Represents a section (set of questions) in the index card
    """
    class Meta:
            ordering = ['code']

    name = django.db.models.CharField(max_length=100, unique=False)
    index_card = django.db.models.ForeignKey(IndexCard)


class Question(Common):
    """
    Abstract class with basic elements of a hazard question
    """
    statement = django.db.models.CharField(max_length=250, null=True, blank=True)
    answer_type = django.db.models.CharField(max_length=1, null=True, blank=True)
    answer_short = django.db.models.CharField(max_length=250, null=True, blank=True)
    answer_long = django.db.models.TextField(null=True, blank=True)
    section = django.db.models.ForeignKey(Section)
    comments = django.db.models.CharField(max_length=400, null=True, blank=True)

class IndexCardService(django.db.models.Model):
    """
    Represents a city service (relationship between city and master service)
    """
    index_card = django.db.models.ForeignKey(IndexCard)
    service = django.db.models.ForeignKey(Service)

class ServiceT1Question(django.db.models.Model):
    """
    Represents question matrix for a service
    """
    population_served = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_1_label = django.db.models.CharField(max_length=100, null=True, blank=True)
    value_1T = django.db.models.CharField(max_length=100, null=True, blank=True)
    value_2T = django.db.models.CharField(max_length=100, null=True, blank=True)
    value_3T = django.db.models.CharField(max_length=100, null=True, blank=True)
    mov = django.db.models.TextField(null=True, blank=True)
    additional_information = django.db.models.TextField(null=True, blank=True)
    index_card_service = django.db.models.ForeignKey(IndexCardService)


class ServiceT2Question(django.db.models.Model):
    """
    Represents question matrix for a service and its components
    """
    population_served = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_1_label = django.db.models.CharField(max_length=100, null=False, blank=True)
    component_2_label = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_1_value_1T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_1_value_2T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_1_value_3T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_2_value_1T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_2_value_2T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_2_value_3T = django.db.models.CharField(max_length=100, null=True, blank=True)
    mov = django.db.models.TextField(null=True, blank=True)
    additional_information = django.db.models.TextField(null=True, blank=True)
    index_card_service = django.db.models.ForeignKey(IndexCardService)


class ServiceT3Question(django.db.models.Model):
    """
    Represents question matrix for a service and its components
    """
    population_served = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_1_label = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_2_label = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_3_label = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_1_value_1T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_1_value_2T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_1_value_3T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_2_value_1T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_2_value_2T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_2_value_3T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_3_value_1T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_3_value_2T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_3_value_3T = django.db.models.CharField(max_length=100, null=True, blank=True)
    mov = django.db.models.TextField(null=True, blank=True)
    additional_information = django.db.models.TextField(null=True, blank=True)
    index_card_service = django.db.models.ForeignKey(IndexCardService)

class ServiceT4Question(django.db.models.Model):
    """
    Represents question matrix for a service and its components
    """
    population_served = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_1_label = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_2_label = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_3_label = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_4_label = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_1_value_1T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_1_value_2T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_1_value_3T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_2_value_1T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_2_value_2T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_2_value_3T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_3_value_1T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_3_value_2T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_3_value_3T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_4_value_1T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_4_value_2T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_4_value_3T = django.db.models.CharField(max_length=100, null=True, blank=True)
    mov = django.db.models.TextField(null=True, blank=True)
    additional_information = django.db.models.TextField(null=True, blank=True)
    index_card_service = django.db.models.ForeignKey(IndexCardService)

class ServiceT5Question(django.db.models.Model):
    """
    Represents question matrix for a service and its components
    """
    population_served = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_1_label = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_2_label = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_3_label = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_4_label = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_5_label = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_1_value_1T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_1_value_2T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_1_value_3T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_2_value_1T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_2_value_2T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_2_value_3T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_3_value_1T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_3_value_2T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_3_value_3T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_4_value_1T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_4_value_2T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_4_value_3T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_5_value_1T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_5_value_2T = django.db.models.CharField(max_length=100, null=True, blank=True)
    component_5_value_3T = django.db.models.CharField(max_length=100, null=True, blank=True)
    mov = django.db.models.TextField(null=True, blank=True)
    additional_information = django.db.models.TextField(null=True, blank=True)
    index_card_service = django.db.models.ForeignKey(IndexCardService)


class CompetenceCategory(django.db.models.Model):
    """
    Represents a competence category of the city
    """
    name = django.db.models.CharField(max_length=100, null=False, blank=False)


class CompetenceComponent(django.db.models.Model):
    """
    Represents a competence component
    """
    name = django.db.models.CharField(max_length=100, null=False, blank=False)
    competence_category = django.db.models.ForeignKey(CompetenceCategory)


class IndexCardCompetenceCategory(django.db.models.Model):
    """
    Represents a competence component for a index card
    """
    index_card = django.db.models.ForeignKey(IndexCard)
    competence_category = django.db.models.ForeignKey(CompetenceCategory)


class Ownership(Common):
    """
    Represents ownership/responsibility entries
    """


class Operator(Common):
    """
    Represents operator entries
    """

class Competence(Common):
    """
    Represents competence entries
    """

class RoleInECPlans(Common):
    """
    Represents roles in E/C plans
    """

class CompetenceQuestion(django.db.models.Model):
    """
    Represents a competence question for a physical component of the city
    """
    label_text = django.db.models.CharField(max_length=100, null=True, blank=True)
    owner = django.db.models.ManyToManyField(Ownership, null=True, blank=True)
    owner_comments = django.db.models.TextField(null=True, blank=True)
    operator = django.db.models.ManyToManyField(Operator, null=True, blank=True)
    operator_comments = django.db.models.TextField(null=True, blank=True)
    competences = django.db.models.ManyToManyField(Competence, null=True, blank=True)
    competences_comments = django.db.models.TextField(null=True, blank=True)
    role_in_ec_plan = django.db.models.ManyToManyField(RoleInECPlans, null=True, blank=True)
    role_in_ec_plan_comments = django.db.models.TextField(null=True, blank=True)
    index_card_competence_category = django.db.models.ForeignKey(IndexCardCompetenceCategory)


class Dimension(Common):
    """
    Represents a dimension of the urban model
    """


class Component(Common):
    """
    Represents a component of a dimension of the model
    """
    dimension = django.db.models.ForeignKey(Dimension)


class System(Common):
    """
    Represents a system of the city. Used to model relation between components in different dimensions
    """
    components = django.db.models.ManyToManyField(Component, null=True, blank=True)


class Element(Common):
    """
    Represents a component of a dimension of the model
    """
    system = django.db.models.ForeignKey(System)
    components = django.db.models.ManyToManyField(Component)


class ResilienceCharacteristic(Common):
    """
    Represents a resilience characteristic
    """

class ResiliencePrinciple(Common):
    """
    Represents a resilience characteristic
    """
    resilience_characteristic = django.db.models.ForeignKey(ResilienceCharacteristic)


class ElementQuestionCharField(Common):
    """
    Represents question with answer charfield
    """
    answer = django.db.models.CharField(max_length=500, null=True, blank=True)
    statement = django.db.models.CharField(max_length=200)
    explanation = django.db.models.CharField(max_length=200, null=True, blank=True)
    score = django.db.models.IntegerField(default=0, null=False, blank=False)
    mov = django.db.models.TextField(null=True, blank=True)
    additional_information = django.db.models.TextField(null=True, blank=True)
    answered = django.db.models.BooleanField(default=False)
    type = django.db.models.CharField(max_length=10)
    resilience_principle = django.db.models.ForeignKey(ResiliencePrinciple)
    element = django.db.models.ForeignKey(Element)
    index_card = django.db.models.ForeignKey(IndexCard)

    def __init__(self, *args, **kwargs):
        """
        try:
            type = kwargs.pop('type')
        except:
            type = str(getattr(self,'type')).strip()
        """
        super(ElementQuestionCharField, self).__init__(*args, **kwargs)
        """
        if str(getattr(self,'type')).strip() == YES_NO_TYPE:
            self._meta.get_field_by_name('answer')[0]._choices = CHOICES_YES_NO
            self._meta.get_field_by_name('answer')[0]._widget = forms.Select()
        if str(getattr(self,'type')).strip() == ENGAGEMT_TYPE:
            self._meta.get_field_by_name('answer')[0]._choices = CHOICES_ENGAGEMENT
            self._meta.get_field_by_name('answer')[0]._widget = forms.Select()
        if str(getattr(self,'type')).strip() == CHAR_TYPE:
            self._meta.get_field_by_name('answer')[0]._widget = forms.CharField()
        """


