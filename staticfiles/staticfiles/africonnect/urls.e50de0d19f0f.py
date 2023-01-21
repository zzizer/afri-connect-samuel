from django.urls import path
from .views import SpecificJobDetailView, OpportunityCreateView,OpportunityDeleteView, OpportunityUpdateView, ServiceInDetail
from . import views

urlpatterns = [
    path('searching/', views.searchingPage, name = 'searching'),
    path('about-africonnect-uganda-ltd', views.about_africonnect, name = 'about-africonnect'),
    path('specificjob/<str:pk>/', SpecificJobDetailView.as_view(), name = 'specificjob'),
    path('addopportunity/<str:pk>/', OpportunityCreateView.as_view(), name = 'new-opportunity'),
    path('update/edit/job/<str:pk>/', OpportunityUpdateView.as_view(), name = 'update-opportunity'),
    path('delete/job/<str:pk>/', OpportunityDeleteView.as_view(), name = 'delete-opportunity'),
    path('specific-service/<str:pk>/', ServiceInDetail.as_view(), name = 'service-details'),
]
