from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta 
from django.utils import timezone
from openpyxl.descriptors.base import Default
from django.contrib.auth.models import User, Group
from django.utils.timezone import now
from datetime import timedelta

def is_pma_admin(user):
    return user.groups.filter(name='PMA Admin').exists()

class Athlete(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='athlete_profile')
    programming_deadline = models.DateField()
    coach = models.ForeignKey(User, on_delete=models.CASCADE, related_name='coaches_athletes')

    def __str__(self):
        return f"{self.user.first_name} ({self.user.username})"

class AthleteDocument(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name='documents')
    document = models.FileField(upload_to='athlete_pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_title = models.CharField(max_length=255, default="Untitled Document")  # Default added here
    description = models.TextField(default="No description provided")  # Default added here
    keywords = models.CharField(max_length=255, default="None", help_text="Comma-separated keywords for search")  # Default added here
    is_csv = models.BooleanField(default=False)
    is_xlsx = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.document and self.document.name:
            if self.document.name.endswith('.csv'):
                self.is_csv = True
                self.is_xlsx = False
            elif self.document.name.endswith('.xlsx'):
                self.is_xlsx = True
                self.is_csv = False
            else:
                self.is_csv = False
                self.is_xlsx = False
        super().save(*args, **kwargs)

class AthleteRoster(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='manager')
    athletes = models.ManyToManyField(Athlete, blank=True, related_name='athletes')

    def __str__(self):
        return f"{self.manager.username} is manager of this roster"

    def add_athlete(self, athlete):
        if not athlete in self.athletes.all():
            self.athletes.add(athlete)

    # Could add remove_athlete method here when needed later
def default_programming_deadline():
    return datetime.now().date() + timedelta(days=30)
class AthleteRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reciever', null=True, blank=True)
    is_active = models.BooleanField(blank=True, null=False, default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    programming_deadline = models.DateField(default=default_programming_deadline)

    def __str__(self):
        return f"{self.sender.username} to {self.receiver.username} at {self.timestamp}"

    def accept(self):
        self.delete()

    def decline(self):
        self.delete()

class FeedbackRequest(models.Model):
    coach = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedback_requests')
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedback_received')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.coach.username} to {self.client.username}"

class FeedbackQuestion(models.Model):
    feedback_request = models.ForeignKey(FeedbackRequest, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    answer = models.TextField(blank=True, null=True)  # This will be filled later by the client

    def __str__(self):
        return f"Question: {self.question_text}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    motivational_quote = models.TextField()
    quote_timedate = models.DateField(default=timezone.now)

    def __str__(self):
            return f"This is {self.user.username}'s profile"

class Video(models.Model):
    document = models.ForeignKey(AthleteDocument, related_name='videos', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date_posted = models.DateField()
    url = models.URLField()
    youtube_id = models.CharField(max_length=11, blank=True, null=True)  # 11-character YouTube ID


    def __str__(self):
        return self.title








