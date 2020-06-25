from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User, Profile


class UserAdmin(BaseUserAdmin):
   

    model = User

    list_display = ('email', 'username','is_staff', 'is_active','is_student',)
    list_filter = ('email', 'is_staff', 'is_active','is_student',)
    fieldsets = (
        (None, {'fields': ('email', 'username','password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_student')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'is_student')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User,UserAdmin)
admin.site.register(Profile)