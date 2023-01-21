from django.urls import path
from . import views
from .views import AddSocialLink, UpdateProfileView, OpportunitiesListView, PasswordsChangeView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('SignIn', views.signin, name='signin'),
    path('SignOut', views.signout, name='signout'),
    path('', OpportunitiesListView.as_view(), name = 'home'),
    path('about/single/user/<str:pk>', views.userDetailView, name='about'),
    path('followers_count', views.followers_count, name='followers_count'),
    path('updateprofile/<str:pk>', UpdateProfileView.as_view(), name='update-profile'),
    path('addlink/socialmedia/<str:pk>', AddSocialLink.as_view(), name='other-socials'),
    path('My_Profile/<str:pk>', views.myProfile, name='myProfile'),
    path('create_personal_account', views.createpersonalaccount, name='create_personal_account'),
    path('create_business_account', views.createbusinessaccount, name='create_business_account'),
    #change password
    path('change-password/', PasswordsChangeView.as_view(template_name='accounts_pages/change-password.html'), name='change-password'),
    #forgot password / resetting security key
    #1
    path('reset_password/', 
    auth_views.PasswordResetView.as_view(template_name='accounts_pages/email_input_reset_password.html'), 
    name='reset_password'),
    #2
    path('password_reset_sent/', 
    auth_views.PasswordResetDoneView.as_view(template_name='accounts_pages/password_reset_sent.html'), 
    name='password_reset_done'),
    #3
    path('reset/<uidb64>/<token>/', 
    auth_views.PasswordResetConfirmView.as_view(template_name='accounts_pages/password_reset_confirm.html'), 
    name='password_reset_confirm'),
    #4
    path('reset_password_complete/', 
    auth_views.PasswordResetCompleteView.as_view(template_name='accounts_pages/password_reset_complete.html'), 
    name='password_reset_complete'),
]