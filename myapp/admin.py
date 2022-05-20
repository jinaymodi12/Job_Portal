from django.contrib import admin
from.models import *

# Register your models here.
class CandidateProfileadmin(admin.ModelAdmin):
    model=CandidateProfile
    list_display = ['name']

class jobpostadmin(admin.ModelAdmin):
    model=JobPost
    list_display = ['user']

admin.site.register(User)
admin.site.register(JobPost,jobpostadmin)
admin.site.register(CandidateProfile,CandidateProfileadmin)