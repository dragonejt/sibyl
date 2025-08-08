from django.contrib import admin

from community.models import Community
from dominator.models import MemberDominator, MessageDominator

# Register your models here.


class MessageDominatorInline(admin.StackedInline):
    model = MessageDominator


class MemberDominatorInline(admin.StackedInline):
    model = MemberDominator


class CommunityAdmin(admin.ModelAdmin):
    model = Community
    inlines = [MessageDominatorInline, MemberDominatorInline]


admin.site.register(Community, CommunityAdmin)
