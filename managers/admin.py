from django.contrib import admin
from managers.models import MessageManager, MemberManager

# Register your models here.

admin.site.register(MessageManager)
admin.site.register(MemberManager)
