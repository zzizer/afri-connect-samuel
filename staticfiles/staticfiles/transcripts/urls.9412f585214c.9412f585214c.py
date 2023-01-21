from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('myCV-homepage/<str:pk>', CVHomePage.as_view(), name='CV-homepage'),
    path('myCV/objective/<str:pk>', ObjectiveCreateView.as_view(), name='add-objective'),
    path('myCV/add-skills/<str:pk>', SkillsCreateView.as_view(), name='add-skills'),
    path('myCV/education-background/<str:pk>', EducationBackgroundCreateView.as_view(), name='add-education-background'),
    path('myCV/add-relevant-docs/<str:pk>', OtherDocumentCreateView.as_view(), name='add-relevant-docs'),
    path('myCV/leadership-exp/<str:pk>', LeadershipExpCreateView.as_view(), name='add-leadership-skills'),
    path('myCV/work-exp/<str:pk>', WorkingExpCreateView.as_view(), name='add-work-experience'),
    path('myCV/languages-Spoken/<str:pk>', LanguageSpokenCreateView.as_view(), name='add-language'),
    path('myCV/reference/<str:pk>', ReferenceCreateView.as_view(), name='add-reference'),
    path('myCV/hobbies/<str:pk>', HobbiesCreateView.as_view(), name='add-hobby'),
    #Create
    path('myCV/update-cv/<str:pk>', ChooseCVUpdateView.as_view(), name='choose-cv'),
    #Preview
    path('myCV/preview/<str:pk>', ResumeDetailView.as_view(), name='preview-cv'),
]
