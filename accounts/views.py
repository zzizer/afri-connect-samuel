from django.shortcuts import render, redirect
from django.views.generic import (
    ListView, CreateView, DetailView, UpdateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import NewUser, FollowersCount
from django.contrib.auth import authenticate
from africonnect.models import Opportunity
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordChangeForm
from django.contrib.auth.decorators import login_required

class PasswordsChangeView(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('myProfile')

    success_message = "Password successfully changed...!"
    login_url = 'signin'

class OpportunitiesListView(ListView):
    model = Opportunity
    paginate_by = 3
    template_name = "afri_apps_pages/index.html"
    ordering = ['-uploaded_on']

def createbusinessaccount(request):    
    if request.method == 'POST':
        email = request.POST['email']
        user_name = request.POST['user_name']
        surname = request.POST['surname']
        given_name = request.POST['given_name']
        telephone_number = request.POST['telephone_number']
        date_of_birth = request.POST['date_of_birth']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            password = pass1
            myUser = NewUser.objects.create_user(email,user_name, password)
            myUser.date_of_birth = date_of_birth
            myUser.given_name = given_name
            myUser.surname = surname
            myUser.telephone_number = telephone_number

            myUser.is_business = True
            myUser.is_active = True
            
            myUser.save()
            messages.info(request, "Business account created Successfully...!")

            return redirect("signin")
        else:
            messages.error(request, "Passwords don't Match")
            return redirect("create_business_account")

    context = {
         messages: 'messages',
    }

    return render(request, 'accounts_pages/createbusinessaccount.html', context)

def createpersonalaccount(request):
    if request.method == 'POST':
        email = request.POST['email']
        user_name = request.POST['user_name']
        surname = request.POST['surname']
        given_name = request.POST['given_name']
        date_of_birth = request.POST['date_of_birth']
        telephone_number = request.POST['telephone_number']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            password = pass1
            myUser = NewUser.objects.create_user(email,user_name, password)
            myUser.date_of_birth = date_of_birth
            myUser.given_name = given_name
            myUser.surname = surname
            myUser.telephone_number = telephone_number

            myUser.is_personal = True
            myUser.is_active = True

            """
            template = render_to_string("accounts_pages/welcome.html", {'surname':surname})
            
            welcome_email = EmailMessage(
                'Welcome to Africonnect Uganda LTD',
                template,
                settings.EMAIL_HOST_USER,
                [email],
            )

            welcome_email.fail_silently = True
            welcome_email.send()
            """

            myUser.save()
            messages.success(request, "Personal account created Successfully...!")

            return redirect("signin")
        else:
            messages.error(request, "Passwords don't Match")
            return redirect("create_personal_account")

    context = {
        messages: 'messages'
    }
    return render(request, 'accounts_pages/createpersonalaccount.html', context)

def signout(request):
    logout(request)
    messages.success(request, 'Logged out successfully...!')
    return redirect('signin')

class UpdateProfileView(SuccessMessageMixin, UpdateView):
    model = NewUser
    template_name = "accounts_pages/update_profile.html"
    fields = [
        'telephone_number','surname', 'given_name', 'date_of_birth', 'about_me', 
    'country', 'physical_address', 'profile_photo'
    ]
    success_message = "Profile successfully updated...!"

def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        myUser = authenticate(email=email, password=password)

        if myUser is not None:
            login(request, myUser)
            messages.success(request, 'Successfully Logged In...!')
            return redirect('home')

        else:
            messages.error(request, 'Wrong Credentials...!')
            return redirect('signin')

    context = {
        messages: 'messages',
    }
    return render(request, 'accounts_pages/in.html', context)

class AddSocialLink(UpdateView):
    model = NewUser
    template_name = 'accounts_pages/add_socialLinks.html'
    fields = [
        'twitter', 'instagram', 'facebook', 'linkedIn', 'git_hub','you_tube'
    ]

    success_message = "Social Links successfully updated"


@login_required(login_url='signin')
def myProfile(request, pk):
    my_profile = NewUser.objects.get(id=pk)

    context = {
         messages: 'messages',
        'my_profile': my_profile,
    }
    return render(request, 'accounts_pages/myProfile.html', context)

@login_required(login_url='signin')
def userDetailView(request, pk):

    thisobject = NewUser.objects.get(id=pk)

    # current_user = request.GET.get('user')
    logged_in_user =  request.user.user_name
    current_user = thisobject.user_name

    user_followers = len(FollowersCount.objects.filter(user=current_user))
    user_following = len(FollowersCount.objects.filter(follower=current_user))

    user_followers0 = FollowersCount.objects.filter(user=current_user)

    user_followers1 = []

    for i in user_followers0:
        user_followers0 = i.follower
        user_followers1.append(user_followers0)

    if logged_in_user in user_followers1:
        follow_button_value = 'unfollow'
    else:
        follow_button_value = 'follow'

    context = {
        'object': thisobject,
        'user_followers':user_followers,
        'user_following':user_following,
        'current_user':current_user,
        'follow_button_value':follow_button_value,
    }

    return render(request, "accounts_pages/aboutme.html", context)

def followers_count(request):
    if request.method == 'POST':
        value = request.POST['value']
        user = request.POST['user']
        follower = request.POST['follower']
    
        if value == 'follow':
            follower_cnt = FollowersCount.objects.create(follower=follower, user=user)
            follower_cnt.save()
        else:
            follower_cnt = FollowersCount.objects.get(follower=follower, user=user)
            follower_cnt.delete()
        
        # print(user)
        return redirect('/')