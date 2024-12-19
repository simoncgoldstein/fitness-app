from django.dispatch import receiver
from allauth.account.signals import user_logged_in
from django.shortcuts import redirect
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(user_logged_in)
def redirect_after_login(sender, request, user, **kwargs):
    return redirect('choose_role')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
