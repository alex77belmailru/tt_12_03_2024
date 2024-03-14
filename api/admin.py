from django.contrib import admin

from api.models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'referral_code', 'is_active', 'is_staff', 'is_superuser',)
    list_editable = ('email', 'referral_code', 'is_active', 'is_staff', 'is_superuser',)
    ordering = ('id',)


@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'owner', 'expiration', 'is_active',)
    list_editable = ('code', 'owner', 'expiration', 'is_active',)
    ordering = ('id',)
