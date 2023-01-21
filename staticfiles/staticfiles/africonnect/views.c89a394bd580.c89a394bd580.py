from django.shortcuts import render, redirect
from .models import Qualifications, Opportunity, NewsFeedSubscribers, ServicesOffered
from .forms import RequirementsForm, NewOpportunityForm
from django.views.generic import (
    ListView, CreateView, DetailView, UpdateView, DeleteView
)
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

@login_required(login_url='signin')
def searchingPage(request):
    if request.method == 'POST':
        searched_is = request.POST['input_text']
        
        comment = f'Results for: {searched_is}'
        
        job = Opportunity.objects.filter(job_title__contains=searched_is)
    else:
        comment = f'Trending: '
        job = Opportunity.objects.all
        
    context = {
        "object_list":job,
        "comment":comment,
    }

    return render(request, "afri_apps_pages/searching.html", context)

def about_africonnect(request):
    services_offered = ServicesOffered.objects.all

    if request.method == 'POST':
        email = request.POST['email']

        if NewsFeedSubscribers.objects.filter(email=email):
            messages.error(request, f"News Feed Subscriber <'{email}'> already exists....!")
            redirect("about-africonnect")
        else:
            subscribers_email = NewsFeedSubscribers.objects.create(email=email)
            subscribers_email.save()
            messages.success(request, f"<'{subscribers_email}'> added to Africonnect NewsFeed Subscribers")
            return redirect("about-africonnect")

    context = {
         messages: 'messages',
         'services':services_offered,
    }

    return render(request, 'afri_apps_pages/about-africonnect.html', context)

class ServiceInDetail(DetailView):
    model = ServicesOffered
    template_name = 'afri_apps_pages/service_in_details.html'

class SpecificJobDetailView(LoginRequiredMixin, DetailView):
    model = Opportunity
    template_name='afri_apps_pages/specificjob.html'

    login_url = 'signin'
    redirect_field_name = 'specificjob'

class OpportunityDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Opportunity
    template_name = 'afri_apps_pages/delete_oppo.html'
    success_url = reverse_lazy('home')

    login_url = 'signin'
    redirect_field_name = 'signin'

    success_message = "Job Opportunity was deleted successfully"
#over-riding
class OpportunityCreateView(SuccessMessageMixin, CreateView):
    model = Opportunity
    form_class = NewOpportunityForm
    template_name = "afri_apps_pages/newopportunity.html"

    success_message = "Job Opportunity was added successfully"

    def form_valid(self, NewOpportunityForm):
        NewOpportunityForm.instance.uploaded_by = self.request.user
        return super().form_valid(NewOpportunityForm)

class OpportunityUpdateView(SuccessMessageMixin, UpdateView):
    model = Opportunity
    template_name = 'afri_apps_pages/update_oppo.html'
    fields = ['Job_type','job_title', 'job_branch', 'uploaded_on', 
    'deadline', 'description', 'qualifications']

    success_message = "Job Opportunity was updated successfully"