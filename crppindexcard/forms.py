from django.forms import ModelForm
from models import Question, ElementQuestionCharField
from django import forms
from constants import *


class QuestionForm(ModelForm):
    """

    """

    class Meta:
        model = Question
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)



class MyForm(forms.ModelForm):

    class Meta:
        model = ElementQuestionCharField
        exclude = []


    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)

        if self.instance:
            if self.instance.type == ENGAGEMT_TYPE:
                self.fields['answer'].widget = forms.Select(choices=CHOICES_ENGAGEMENT)
                #self.fields['answer'] = OPTION_BLANK
            if self.instance.type == YES_NO_TYPE:
                self.fields['answer'].widget = forms.Select(choices=CHOICES_YES_NO)
                #self.fields['answer'] = OPTION_BLANK
        if self.initial:
            if self.initial['type'] == ENGAGEMT_TYPE:
                self.fields['answer'].widget = forms.Select(choices=CHOICES_ENGAGEMENT)
                #self.initial['answer'] = OPTION_BLANK
            if self.initial['type'] == YES_NO_TYPE:
                self.fields['answer'].widget = forms.Select(choices=CHOICES_YES_NO)
                #self.initial['answer'] = OPTION_BLANK


            #self.fields['answer'].widget = forms.Select(choices=CHOICES_YES_NO)

            #self.fields['mov'] = self.fields['type']

            #if self.__class__.Meta.model.type.strip() == YES_NO_TYPE:

            #if str(self.fields['type']).strip() == YES_NO_TYPE:


            #form.__dict__["fields"]["anwser"]
            #self.fields['type'].widget = forms.HiddenInput()





