from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .models import Athlete, AthleteRequest
from .models import AthleteDocument
from .models import FeedbackRequest, FeedbackQuestion

class ClientRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Assign the user to the 'Client' group
            client_group, created = Group.objects.get_or_create(name='Client')
            user.groups.add(client_group)
        return user

class CoachRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Assign the user to the 'Coach' group
            coach_group, created = Group.objects.get_or_create(name='Coach')
            user.groups.add(coach_group)
        return user

# New AthleteForm for adding athletes in coach dashboard
class AthleteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Get the logged-in user from the form's initial data
        self.coach = kwargs.pop('coach', None)
        super(AthleteForm, self).__init__(*args, **kwargs)
        # Filter out the logged-in coach from the list of users
        if self.coach:
            self.fields['user'].queryset = User.objects.exclude(id=self.coach.id)

    user = forms.ModelChoiceField(
        queryset=User.objects.none(),
        label='Select User',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Athlete
        fields = ['user', 'programming_deadline']
        widgets = {
            'programming_deadline': forms.SelectDateWidget(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        athlete_request = AthleteRequest(sender=self.coach, receiver=self.cleaned_data['user'], programming_deadline=self.cleaned_data['programming_deadline']) 

        if commit:
            athlete_request.save()
        return athlete_request

#Uploading file form
class UploadFileForm(forms.ModelForm):
    class Meta:
        model = AthleteDocument
        fields = ['document', 'file_title', 'description', 'keywords']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class FeedbackQuestionForm(forms.ModelForm):
    class Meta:
        model = FeedbackQuestion
        fields = ['question_text']
        widgets = {
            'question_text': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
        }

FeedbackFormSet = forms.formset_factory(FeedbackQuestionForm, extra=5, max_num=5, min_num=1)
      
