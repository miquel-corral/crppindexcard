# from django.db import models
import django.db.models


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


class Section(Common):
    """
    Represents a section (set of questions) in the index card
    """
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


class CompetenceQuestion(django.db.models.Model):
    """
    Represents a competence question for a physical component of the city
    """
    label_text = django.db.models.CharField(max_length=100, null=True, blank=True)
    owner = django.db.models.TextField(null=True, blank=True)
    operator = django.db.models.TextField(null=True, blank=True)
    competences = django.db.models.TextField(null=True, blank=True)
    index_card = django.db.models.ForeignKey(IndexCard)


class HardInfrastructure(django.db.models.Model):
    """
    Represents a hard infrastructure of the city
    """
    name = django.db.models.CharField(max_length=100, null=False, blank=False)


class IndexCardHardInfrastructure(django.db.models.Model):
    """
    Represents a hard infrastructure element competences question for an indexcard
    """
    hard_infrastructure = django.db.models.ForeignKey(HardInfrastructure)
    index_card = django.db.models.ForeignKey(IndexCard)
    competence_question = django.db.models.ForeignKey(CompetenceQuestion)

class BuiltEnvironmentComponent(django.db.models.Model):
    """
    Represents a component of the built environment of the city
    """
    name = django.db.models.CharField(max_length=100, null=False, blank=False)

class IndexCardBuiltEnvironmentComponent(django.db.models.Model):
    """
    Represents competence question for an indexcard built environment component
    """
    index_card = django.db.models.ForeignKey(IndexCard)
    competence_question = django.db.models.ForeignKey(CompetenceQuestion)


class EnvironmentComponent(django.db.models.Model):
    """
    Represents an environment component
    """
    name = django.db.models.CharField(max_length=100, null=False, blank=False)

class IndexCardEnvironmentComponent(django.db.models.Model):
    """
    Represents a competence question for an indexcard environment component
    """
