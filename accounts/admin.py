from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from . import forms


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = forms.CustomUserCreationForm
    form = forms.CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'age', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', 'national_id')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age', 'national_id')})
    )


admin.site.register(CustomUser, CustomUserAdmin)
