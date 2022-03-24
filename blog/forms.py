from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper

from django import forms

from .models import *


class CommetForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ["content"]

  def __init__(self, *args, **kwargs):
    super(CommetForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.add_input(Submit('submit', 'Submit'))
    