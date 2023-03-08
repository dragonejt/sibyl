from django.contrib import admin
from psychopass.models import UserPsychoPass, CommunityPsychoPass

# Register your models here.

admin.site.register(UserPsychoPass)
admin.site.register(CommunityPsychoPass)