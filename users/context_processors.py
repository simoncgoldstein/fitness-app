from django.contrib.auth.models import Group

def is_admin_user(request):
    """
    Add `is_admin` to the context if the user is in the PMA Admin group.
    """
    if request.user.is_authenticated:
        return {
            'is_admin': request.user.groups.filter(name='PMA Admin').exists()
        }
    return {
        'is_admin': False
    }