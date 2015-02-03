RECURRENCE_LABEL = 'Recurrence (T)'
RECURRENCE_COMMENT_LABEL = 'Specify if based in past of expected events'

IT_LABEL_1 = 'Immediate Term'
IT_LABEL_2 = '(1 year)'
ST_LABEL_1 = 'Short Term'
ST_LABEL_2 = '(2-5 years)'
MT_LABEL_1 = 'Mid Term'
MT_LABEL_2 = '(5-10 years)'
LT_LABEL_1 = 'Long Term'
LT_LABEL_2 = '(>10 years)'

INTENSITY = 'Intensity'
NO_LOSSES = 'No significant losses'
DISRUPTION_FUNCTION = 'Disruption function'
MATERIAL_LOSSES = 'Material losses'
CASUALTIES = 'Casualties'

NUMBER_OF_EVENTS = 'Number of events'

MOV = 'Means of verification'
MOV_COMMENTS_HAZARD = 'Official reports for past events/assessment based estimation for future events'
ADDITIONAL_INFO = 'Additional information'
ADDITIONAL_INFO_HAZARD = 'Different affectation in different areas, main disruptions..'

PERIOD_OF_DISRUPTION = 'Period of disruption'
POPULATION_SERVED = 'Population served (%)'
POPULATION_AFFECTED_20 = 'Number of events with >20% population affected'
TERM_8H = '>8h/day'
TERM_24H = '>24h'
TERM_48H = '>48h'
TERM_1W = '>1week'


NUMBER_OF_EVENTS_MONTH = 'Number of events/month with > 20% population affected'
GAS_TRANSPORT_NETWORK = 'Part of the network that carries the supply without reaching the final user, generally at a \
    higher pressure (ex: transport until reduction pressure stations)'
GAS_DISTRIBUTION_NETWORK = 'Part of the network that connects the service to the final user, generally at low pressure'
PLEASE_SPECIFY = 'Please specify'


OWNER_RESPONSIBLE_LABEL = 'Owner/Responsible'
OPERATOR_LABEL = 'Operator'
COMPETENCES_LABEL = 'Competences of the local gov.'
EC_ROLE_LABEL = 'Role in E/C Plans'

COMPETENCES_EXPLANATION_1 = 'Define the owner/responsible for the infrastructure or service, the competences of your' \
    'local government and its role in Emergency/Contingency plans.'
COMPETENCES_EXPLANATION_2 = 'More then one option can be selected. Add any comment or additional information ' \
    'you consider in the text boxes below the selection options.'

def get_recurrence_label():
    return RECURRENCE_LABEL

def get_recurrence_comment_label():
    return RECURRENCE_COMMENT_LABEL

def get_it_label_1():
    return IT_LABEL_1

def get_it_label_2():
    return IT_LABEL_2

def get_st_label_1():
    return ST_LABEL_1

def get_st_label_2():
    return ST_LABEL_2

def get_mt_label_1():
    return MT_LABEL_1

def get_mt_label_2():
    return MT_LABEL_2

def get_lt_label_1():
    return LT_LABEL_1

def get_lt_label_2():
    return LT_LABEL_2

def get_intensity_label():
    return INTENSITY

def get_no_losses_label():
    return NO_LOSSES

def get_disruption_function_label():
    return DISRUPTION_FUNCTION

def get_material_losses_label():
    return MATERIAL_LOSSES

def get_casualties_label():
    return CASUALTIES

def get_number_of_events_label():
    return NUMBER_OF_EVENTS

def get_mov_label():
    return MOV

def get_mov_comments_hazard_label():
    return MOV_COMMENTS_HAZARD

def get_additional_info_label():
    return ADDITIONAL_INFO

def get_additional_info_hazards_label():
    return ADDITIONAL_INFO_HAZARD


def get_period_of_disruption_label():
    return PERIOD_OF_DISRUPTION

def get_population_served_label():
    return POPULATION_SERVED

def get_population_affected_20_label():
    return POPULATION_AFFECTED_20

def get_term_8h_label():
    return TERM_8H

def get_term_24h_label():
    return TERM_24H

def get_term_48h_label():
    return TERM_48H

def get_term_1W_label():
    return TERM_1W

def get_number_of_events_month_label():
    return NUMBER_OF_EVENTS_MONTH

def get_gas_transport_network_label():
    return GAS_TRANSPORT_NETWORK

def gas_distribution_network_label():
    return GAS_DISTRIBUTION_NETWORK

def get_please_specify_label():
    return PLEASE_SPECIFY

def get_owner_responsible_label():
    return OWNER_RESPONSIBLE_LABEL

def get_operator_label():
    return OPERATOR_LABEL

def get_competences_label():
    return COMPETENCES_LABEL


def get_ec_role_label():
    return EC_ROLE_LABEL


def get_competences_explanation_1_label():
    return COMPETENCES_EXPLANATION_1


def get_competences_explanation_2_label():
    return COMPETENCES_EXPLANATION_2