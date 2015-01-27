from django.forms import ModelForm
from models import Question
import django.db
from django.db import models


class QuestionForm(ModelForm):
    """

    """

    class Meta:
        model = Question
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)









