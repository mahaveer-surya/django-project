from django.contrib import admin
from .models import GymMember

@admin.register(GymMember)
class GymMemberAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'membership_type', 'join_date']
