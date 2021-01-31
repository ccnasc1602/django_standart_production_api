from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .models import User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    model = User
    list_display = ['username', ]
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        (None, {'fields': ('mobile_number', 'birth_date')}),
    )