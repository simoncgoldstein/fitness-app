from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from .models import AthleteRequest, Athlete, AthleteRoster, AthleteDocument

# Unregister the default User model
admin.site.unregister(User)

# Register custom User admin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # List of allowed emails
        allowed_emails = ['fgv9zx@virginia.edu', 'cherratusa@gmail.com	']

        # Check if the user's email is in the allowed list
        if obj.email in allowed_emails:
            # Get or create the PMA Admin group
            pma_admin_group, created = Group.objects.get_or_create(name='PMA Admin')

            # Add the user to the group if not already added
            if not obj.groups.filter(name='PMA Admin').exists():
                obj.groups.add(pma_admin_group)
                obj.save()  # Save changes to the user instance

# Define admin classes with specific configurations
class AthleteRequestAdmin(admin.ModelAdmin):
    list_display = ['sender', 'receiver', 'programming_deadline']
    search_fields = ['sender__username', 'receiver_username']
    list_filter = ['programming_deadline']
    readonly_fields = ['sender', 'receiver']

class AthleteAdmin(admin.ModelAdmin):
    list_display = ['user', 'programming_deadline', 'coach']
    search_fields = ['user__username']

class AthleteRosterAdmin(admin.ModelAdmin):
    list_display = ['manager']
    search_fields = ['manager']

# Register models with their respective admin classes
admin.site.register(AthleteRequest, AthleteRequestAdmin)
admin.site.register(Athlete, AthleteAdmin)
admin.site.register(AthleteRoster, AthleteRosterAdmin)
admin.site.register(AthleteDocument)

