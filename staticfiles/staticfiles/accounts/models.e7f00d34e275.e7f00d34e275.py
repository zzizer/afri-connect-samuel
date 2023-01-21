from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
from datetime import date
import uuid
from transcripts.models import *

class CustomAccountManager(BaseUserManager):

    def create_business(self, email, user_name, password, **other_fields):

        other_fields.setdefault('is_business', True)
        other_fields.setdefault('is_verified', True)
        other_fields.setdefault('is_active', True)

        return self.create_user(email, user_name, password, **other_fields)

    def create_personal(self, email, user_name, password, **other_fields):

        other_fields.setdefault('is_verified', True)
        other_fields.setdefault('is_personal', True)
        other_fields.setdefault('is_active', True)

        return self.create_user(email, user_name, password, **other_fields)

    def create_superuser(self, email, user_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_verified', True)


        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff = True.'
            )
        
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser = True.'
            )

        return self.create_user(email, user_name, password, **other_fields)
    
    def create_user(self, email, user_name, password, **other_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, password=password, **other_fields)
        
        user.set_password(password)
        user.save()
        return user

class NewUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(auto_created=True, primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    email = models.EmailField(_('Email address'), max_length=254, unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    given_name = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True)
    telephone_number = PhoneNumberField()
    date_of_birth = models.DateField(auto_now_add=False, blank=True, null=True)
    
    #Other Social Media Plattforms
    linkedIn = models.CharField(default='linkedIn.com', max_length=50)
    git_hub = models.CharField(default='github.com', max_length=50)
    you_tube = models.CharField(default='youtube.com', max_length=50)
    instagram = models.CharField(default='instagram.com', max_length=50)
    facebook = models.CharField(default='facebook.com', max_length=50)
    twitter = models.CharField(default='twitter.com', max_length=50)
 
    #complete Profile
    profile_photo = models.ImageField(blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)
    physical_address = models.CharField(max_length=100, blank=True, null=True)
    country = CountryField(blank=True, null=True)

    #User Cv Details
    other_document = models.ManyToManyField(OtherDocument, blank=True)
    skills = models.ManyToManyField(Skills, blank=True)
    working_experience = models.ManyToManyField(WorkingExperience, blank=True)
    leadership_skills = models.ManyToManyField(LeadershipSkills, blank=True)
    education_background = models.ManyToManyField(AcademicDocument, blank=True)
    hobby = models.ManyToManyField(Hobbies, blank=True)
    objective = models.OneToOneField(Objective, on_delete=models.CASCADE,blank=True,null=True)
    reference = models.ManyToManyField(References, blank=True)
    language_spoken = models.ManyToManyField(LanguagesSpoken, blank=True)

    #More Verification
    is_active = models.BooleanField(default=False)

    is_business = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_personal = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'telephone_number']

    @property
    def imageURL(self):
        try:
            url = self.profile_photo.url
        except:
            url = '' #apps_images/logo.jpg
        return url

    def __str__(self):
        return f'{self.email}'
    
    def age(self):
        years = date.today().year- self.date_of_birth.year
        months = date.today().month- self.date_of_birth.month
        days = date.today().day- self.date_of_birth.day

        age = f'{years} yrs, {months} months and {days} days'
        return age

    def get_absolute_url(self):
        return reverse("myProfile", kwargs={"pk": self.pk})   
    
    class Meta:
        verbose_name  = 'New Account / User'

class FollowersCount(models.Model):
    follower = models.CharField(max_length=50000)
    user = models.CharField(max_length=50000)

    def __str__(self):
        return f'{self.follower} follows {self.user}'
    
    class Meta:
        verbose_name  = 'Follower'
