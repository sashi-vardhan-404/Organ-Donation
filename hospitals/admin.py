from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin  # Use BaseUserAdmin to avoid name clash

# Define a new UserAdmin class
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('province', 'hospital_name', 'country', 'contact_number')}),
    )

# Register the modified UserAdmin with the User model
admin.site.register(User, UserAdmin)  # Register the new UserAdmin
