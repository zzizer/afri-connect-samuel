from django.contrib import admin
from .models import Objective, Skills, AcademicDocument, LeadershipSkills, OtherDocument, WorkingExperience, LanguagesSpoken, References, Hobbies


admin.site.register(Skills)
admin.site.register(AcademicDocument)
admin.site.register(LeadershipSkills)
admin.site.register(OtherDocument)
admin.site.register(WorkingExperience)
admin.site.register(LanguagesSpoken)
admin.site.register(References)
admin.site.register(Hobbies)
admin.site.register(Objective)