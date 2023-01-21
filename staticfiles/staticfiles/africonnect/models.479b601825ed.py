from django.db import models
from datetime import date
import uuid
from accounts.models import NewUser
from django.urls import reverse

class Qualifications(models.Model):
    uploaded_by = models.ForeignKey(NewUser, on_delete=models.CASCADE, blank=True, null=True)
    qualification_or_requirement = models.TextField()

    def __str__(self):
        return self.qualification_or_requirement

    class Meta:
        verbose_name  = 'Qualification'
    
class Opportunity(models.Model):
    choice = [('Internship','Internship'), 
    ('Graduate Trainee','Graduate Trainee'),
    ('Full working Employee','Full working Employee'),
    ('Part working Employee','Part working Employee')]

    uploaded_by = models.ForeignKey(NewUser, on_delete=models.CASCADE, blank=True, null=True)
    Job_type = models.CharField(choices=choice, max_length=100)
    job_title = models.CharField(max_length=50)
    job_branch = models.CharField(max_length=500,blank=True, null=True)
    uploaded_on = models.DateField(auto_now=False, auto_now_add=False)
    deadline = models.DateField(auto_now=False, auto_now_add=False)
    description = models.TextField()
    qualifications = models.ManyToManyField(Qualifications, blank=True)

    def get_absolute_url(self):
        return reverse("home")

    def __str__(self):
        return self.job_title
    
    @property
    def status(self):
        if(self.uploaded_on != None):
            if (date.today().day <= self.deadline.day):
                if (date.today().month <= self.deadline.month):
                    if (date.today().year <= self.deadline.year):
                        status = 'Still Open'
                    else:
                        status = 'Closed'
                    return status
                    
                else:
                    status = 'Closed'
                return status
            else:
                status = 'Closed'
            return status
    
    class Meta:
        verbose_name  = 'Opportunitie'

class NewsFeedSubscribers(models.Model):
    email = models.EmailField(max_length=254, null=False, unique=True, blank=False)

    class Meta:
        verbose_name = 'News Feed Subscriber'

    def __str__(self):
        return self.email

class ServicesOffered(models.Model):
    title = models.CharField(blank=True, max_length=500)
    simple_logo_to_service = models.ImageField(blank=True)
    brief_description = models.TextField(blank=True, null=True)
    description_in_details = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Offered Service'

    def __str__(self):
        return self.title
    
    @property
    def imageURL(self):
        try:
            url = self.simple_logo_to_service.url
        except:
            url = ''
        return url