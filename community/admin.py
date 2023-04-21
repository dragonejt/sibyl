from django.contrib import admin
from community.models import Community
from dominator.models import MessageDominator, MemberDominator
from psychopass.models import CommunityPsychoPass

# Register your models here.


class CommunityPsychoPassInline(admin.StackedInline):
    model = CommunityPsychoPass


class MessageDominatorInline(admin.StackedInline):
    model = MessageDominator


class MemberDominatorInline(admin.StackedInline):
    model = MemberDominator


class CommunityAdmin(admin.ModelAdmin):
    model = Community
    inlines = [CommunityPsychoPassInline,
               MessageDominatorInline, MemberDominatorInline]


admin.site.register(Community, CommunityAdmin)
