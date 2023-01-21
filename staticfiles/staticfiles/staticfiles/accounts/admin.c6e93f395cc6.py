from django.contrib import admin
from .models import NewUser, FollowersCount

admin.site.register(FollowersCount)

@admin.register(NewUser)
class NewUserAdmin(admin.ModelAdmin):
    search_fields = ('email', 'surname', 'telephone_number', 'is_personal', 'is_business', 'is_superuser',)
    
    list_filter = ['email', 'user_name', 'is_business', 'is_superuser', 'is_personal']

    list_display = [
        'email','surname','given_name','is_personal', 'is_business', 'is_superuser','is_verified', 'is_active'
    ]

    fieldsets = (
        (None, {
            "fields": (
                'email', 'user_name', 'surname','given_name','profile_photo',
            ),
        }),
        
        ('Permissions', {
            "fields": (
                'is_staff', 'is_active', 'is_personal', 'is_business','is_verified',
            ),
        }),

        ('Contact & Personal Info', {
            "fields": (
                'about_me','date_of_birth', 'telephone_number', 'physical_address','country',
            ),
        }),

        ('Other Media Plattforms', {
            "fields": (
                'linkedIn','git_hub', 'you_tube', 'facebook','twitter', 'instagram',
            ),
        }),

        ('Resume Details', {
            "fields": (
                'objective','skills','other_document', 'working_experience', 'leadership_skills','language_spoken', 'hobby', 'reference','education_background',
            ),
        }),
        
        ('Security', {
            "fields": (
                'password', 'last_login'
            ),
        }),
    )   