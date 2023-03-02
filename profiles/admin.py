from django.contrib import admin
from profiles.models import UserProfile, CommunityProfile

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(CommunityProfile)