from django.contrib import admin
from dominator.models import MemberDominator, MessageDominator

# Register your models here.

admin.site.register(MemberDominator)
admin.site.register(MessageDominator)
