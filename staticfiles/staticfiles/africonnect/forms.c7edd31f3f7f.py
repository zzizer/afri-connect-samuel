#forms
from .models import Opportunity, Qualifications
from django import forms

class NewOpportunityForm(forms.ModelForm):
    class Meta:
        model = Opportunity
        fields = '__all__'

class RequirementsForm(forms.ModelForm):
    class Meta:
        model = Qualifications
        fields = '__all__'