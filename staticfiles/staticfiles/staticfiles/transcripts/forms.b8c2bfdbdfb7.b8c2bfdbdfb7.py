from .models import (
    Objective, Skills, AcademicDocument, LeadershipSkills, 
    OtherDocument, WorkingExperience, LanguagesSpoken, References, Hobbies)
from django import forms
from accounts.models import NewUser

class ObjectiveForm(forms.ModelForm):
    class Meta:
        model = Objective
        fields = '__all__'

class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'

class AcademicDocumentForm(forms.ModelForm):
    class Meta:
        model = AcademicDocument
        fields = '__all__'

class LeadershipSkillsForm(forms.ModelForm):
    class Meta:
        model = LeadershipSkills
        fields = '__all__'

class OtherDocumentForm(forms.ModelForm):
    class Meta:
        model = OtherDocument
        fields = '__all__'
class WorkingExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkingExperience
        fields = '__all__'
class ObjectiveForm(forms.ModelForm):
    class Meta:
        model = Objective
        fields = '__all__'
class ReferencesForm(forms.ModelForm):
    class Meta:
        model = References
        fields = '__all__'
class LanguagesSpokenForm(forms.ModelForm):
    class Meta:
        model = LanguagesSpoken
        fields = '__all__'
class HobbiesForm(forms.ModelForm):
    class Meta:
        model = Hobbies
        fields = '__all__' 
class ResumeForm(forms.ModelForm):
    class Meta:
        model = NewUser
        fields = '__all__'