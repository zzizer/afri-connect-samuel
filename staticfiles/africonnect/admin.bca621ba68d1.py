from django.contrib import admin
from .models import Qualifications, Opportunity, NewsFeedSubscribers, ServicesOffered

admin.site.register(Qualifications)
admin.site.register(Opportunity)
admin.site.register(NewsFeedSubscribers)
admin.site.register(ServicesOffered)