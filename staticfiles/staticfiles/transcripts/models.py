from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse

class Objective(models.Model):
    objective_statement = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("CV-homepage", kwargs={'pk':self.pk})
    
    class Meta:
        verbose_name  = 'Objective'

    def __str__(self):
        return self.objective_statement
    
class References(models.Model):
    name_of_refere = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    email = models.EmailField(max_length=254)
    institution_name = models.CharField(max_length=50)
    working_as = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse("CV-homepage", kwargs={'pk':self.pk})

    def __str__(self):
        return self.name_of_refere
    
    class Meta:
        verbose_name  = 'Reference'

class Hobbies(models.Model):
    hobby_name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse("CV-homepage", kwargs={'pk':self.pk})

    class Meta:
        verbose_name  = 'Hobbie'

    def __str__(self):
        return self.hobby_name

class LanguagesSpoken(models.Model):
    levels = [('Excellent','Excellent'), 
    ('Good','Good'),
    ('Fairly Good','Fairly Good'),
    ('Poor','Poor')]
    language_name = models.CharField(max_length=50)
    level_of_proficiency = models.CharField(choices=levels, max_length=250)

    def get_absolute_url(self):
        return reverse("CV-homepage", kwargs={'pk':self.pk})
    
    class Meta:
        verbose_name  = 'Language'

    def __str__(self):
        return self.language_name
    
class Skills(models.Model):
    levels = [('Excellent','Excellent'), 
    ('Good','Good'),
    ('Fairly Good','Fairly Good'),
    ('Poor','Poor')]
    skills_name = models.CharField(max_length=150)
    level_of_proficiency = models.CharField(choices=levels, max_length=250)

    def get_absolute_url(self):
        return reverse("CV-homepage", kwargs={'pk':self.pk})
    
    class Meta:
        verbose_name  = 'Skill'

    def __str__(self):
        return self.skills_name

class AcademicDocument(models.Model):
    year_from = models.DateField(auto_now_add=False, blank=True, null=True)
    year_to = models.DateField(auto_now_add=False, blank=True, null=True)
    institution_name = models.CharField(max_length=100, blank=True, null=True)
    award = models.CharField(max_length=100, blank=True, null=True)
    copy_of_document = models.FileField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("CV-homepage", kwargs={'pk':self.pk})

    def __str__(self):
        return self.institution_name

class LeadershipSkills(models.Model):
    year_from = models.DateField(auto_now_add=False, blank=True, null=True)
    year_to = models.DateField(auto_now_add=False, blank=True, null=True)
    institution_name = models.CharField(max_length=100, blank=True, null=True)
    post = models.CharField(max_length=100, blank=True, null=True)
    certificate = models.FileField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("CV-homepage", kwargs={'pk':self.pk})

    def __str__(self):
        return self.institution_name

class WorkingExperience(models.Model):
    year_from = models.DateField(auto_now_add=False, blank=True, null=True)
    year_to = models.DateField(auto_now_add=False, blank=True, null=True)
    institution_name = models.CharField(max_length=100, blank=True, null=True)
    post = models.CharField(max_length=100, blank=True, null=True)
    certificate = models.FileField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("CV-homepage", kwargs={'pk':self.pk})

    def __str__(self):
        return self.institution_name
    
class OtherDocument(models.Model):
    document_name = models.CharField(max_length=100, blank=True, null=True)
    issued_by = models.CharField(max_length=100, blank=True, null=True)
    copy_of_document = models.FileField(blank=True, null=True)
    NIN_or_Identifier_Number = models.CharField(max_length=150, blank=True)
    expires_on = models.DateField(auto_now_add=False, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("CV-homepage", kwargs={'pk':self.pk})   

    def __str__(self):
        return self.document_name
    class Meta:
        verbose_name  = 'Other Doc'