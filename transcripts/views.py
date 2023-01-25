from django.shortcuts import render
from .forms import (
    ObjectiveForm, OtherDocumentForm, AcademicDocumentForm, HobbiesForm,
    LeadershipSkillsForm, WorkingExperienceForm, ReferencesForm,
    SkillsForm, LanguagesSpokenForm
)
from .models import (
    Objective, OtherDocument, AcademicDocument, Hobbies,
    LeadershipSkills, WorkingExperience, References,
    Skills, LanguagesSpoken
)
from accounts.models import NewUser
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView, TemplateView
from django.contrib.auth.decorators import login_required
class ChooseCVUpdateView(UpdateView):
    model = NewUser
    template_name = 'cv/choose.html'
    fields = [
        'objective','education_background', 'skills', 'leadership_skills', 
        'working_experience','other_document', 'hobby', 'language_spoken', 'reference'
    ]

@login_required(login_url='signin')
def myReverse(request):
    return render(request, "reverse/reverse.html")
class ResumeDetailView(DetailView):
    model = NewUser
    template_name = 'cv/preview-cv.html'

@login_required(login_url='signin')
def CVHomePage(request, pk):
    object = NewUser.objects.get(id=pk)
    context = {
        "object":object
    }
    return render(request, 'cv/CV-index.html', context)
class HobbiesCreateView(CreateView):
    model = Hobbies
    form_class = HobbiesForm
    template_name = 'cv/hobbies.html'

class SkillsCreateView(CreateView):
    model = Skills
    form_class = SkillsForm
    template_name = 'cv/skills.html'

    def form_valid(self, SkillsForm):
        SkillsForm.instance.uploaded_by = self.request.user
        return super().form_valid(SkillsForm)

class EducationBackgroundCreateView(CreateView):
    model = AcademicDocument
    form_class = AcademicDocumentForm
    template_name = 'cv/education.html'

    def form_valid(self, AcademicDocumentForm):
        AcademicDocumentForm.instance.uploaded_by = self.request.user
        return super().form_valid(AcademicDocumentForm)

class OtherDocumentCreateView(CreateView):
    model = OtherDocument
    form_class = OtherDocumentForm
    template_name = 'cv/relevant_documents.html'


class LanguageSpokenCreateView(CreateView):
    model = LanguagesSpoken
    form_class = LanguagesSpokenForm
    template_name = 'cv/languages.html'

    def form_valid(self, LanguagesSpokenForm):
        LanguagesSpokenForm.instance.uploaded_by = self.request.user
        return super().form_valid(LanguagesSpokenForm)

class LeadershipExpCreateView(CreateView):
    model = LeadershipSkills
    form_class = LeadershipSkillsForm
    template_name = 'cv/leadershipskills.html'

    def form_valid(self, LeadershipSkillsForm):
        LeadershipSkillsForm.instance.uploaded_by = self.request.user
        return super().form_valid(LeadershipSkillsForm)

class ReferenceCreateView(CreateView):
    model = References
    form_class = ReferencesForm
    template_name = 'cv/reference.html'

    def form_valid(self, ReferencesForm):
        ReferencesForm.instance.uploaded_by = self.request.user
        return super().form_valid(ReferencesForm)
    
class WorkingExpCreateView(CreateView):
    model = WorkingExperience
    form_class = WorkingExperienceForm
    template_name = 'cv/working_experience.html'

    def form_valid(self, WorkingExperienceForm):
        WorkingExperienceForm.instance.uploaded_by = self.request.user
        return super().form_valid(WorkingExperienceForm)

class ObjectiveCreateView(CreateView):
    model = Objective
    form_class = ObjectiveForm
    template_name = 'cv/objective.html'

    # def form_valid(self, ObjectiveForm):
    #     ObjectiveForm.instance.uploaded_by = self.request.user
    #     return super().form_valid(ObjectiveForm)
