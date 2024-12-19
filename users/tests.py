from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Athlete, AthleteDocument, AthleteRoster
from datetime import datetime, timedelta
from django.core.files.uploadedfile import SimpleUploadedFile

User = get_user_model()

class LoginTests(TestCase):

    def setUp(self):
        client =  User.objects.create(username = "client", password = "password123")
        coach =  User.objects.create(username = "coach", password = "password123")

    # Test for validating redirect to user_dashboard
    def test_user_dashboard_redirect(self):
        response = self.client.get(reverse('choose_role'))
        self.assertEqual(response.status_code, 302)


    # Test for validating redirect to coach_dashboard
    def test_coach_dashboard_redirect(self):
        response = self.client.get(reverse('choose_role'))
        self.assertEqual(response.status_code, 302)


# Model Tests
class AthleteTests(TestCase):

    def setUp(self):
        self.athlete_user = User.objects.create(username="client", password = "password123")
        self.coach =  User.objects.create(username = "coach", password = "password123")

        self.athlete = Athlete.objects.create(
                user = self.athlete_user,
                programming_deadline=datetime.now().date() + timedelta(days=30),
                coach = self.coach
                )

    def test_athlete_str_method(self):
        self.assertEqual(str(self.athlete).strip(), f"{self.athlete_user.first_name} ({self.athlete_user.username})".strip())

    def test_athlete_coach_relationship(self):
        self.assertEqual(self.athlete.coach, self.coach)


class AthleteDocumentModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='client', password='password123') 
        self.athlete = Athlete.objects.create(
                user = self.user,
                coach = self.user,
                programming_deadline=datetime.now().date() + timedelta(days=30)
                )
        self.document = AthleteDocument.objects.create(
                    athlete=self.athlete,
                    document = 'testfile.csv',
                    file_title = 'testfile',
                    keywords = 'sample, document',
                )

    
    def test_save_function(self):
        self.assertEqual(str(self.document.file_title), 'testfile')

    def test_current_file_format(self):
        self.document.save()
        self.assertTrue(self.document.is_csv)
        self.assertFalse(self.document.is_xlsx)


    def test_file_format_change(self):
        self.document.document = 'testfile.xlsx'
        self.document.save()
        self.assertFalse(self.document.is_csv)
        self.assertTrue(self.document.is_xlsx)

class AthleteRosterTests(TestCase):

    def setUp(self):
        self.athlete_user = User.objects.create(username='client', password='password123') 
        self.manager=  User.objects.create(username = "coach", password = "password123")
        self.roster = AthleteRoster.objects.create(manager=self.manager)

        self.athlete = Athlete.objects.create(
                user = self.athlete_user,
                coach = self.manager,
                programming_deadline=datetime.now().date() + timedelta(days=30)
                )

    def test_roster_str_method(self):
        self.assertEqual(str(self.roster), f"{self.manager.username} is manager of this roster")


    def test_add_to_roster(self):
       self.roster.add_athlete(self.athlete) 
       self.assertIn(self.athlete, self.roster.athletes.all())


class AthleteFileUploadTests(TestCase):

    def setUp(self):
        self.athlete_user = User.objects.create(username='client', password='password123') 
        self.manager=  User.objects.create(username = "coach", password = "password123")
        self.roster = AthleteRoster.objects.create(manager=self.manager)

        self.athlete = Athlete.objects.create(
                user = self.athlete_user,
                coach = self.manager,
                programming_deadline=datetime.now().date() + timedelta(days=30)
                )

        self.roster.add_athlete(self.athlete) 
        self.url = reverse('upload_form', args=[self.athlete.id])


    def test_pdf_file_upload(self):
        test_file = SimpleUploadedFile("dummyfile.pdf", b"file content", content_type="application/pdf")
        
        response = self.client.post(self.url, {
            "document" : test_file,
            "file_title" : "dummyfile",
            "description" : "N/A",
            "keywords" : "test_file"
            })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(AthleteDocument.objects.filter(athlete=self.athlete, file_title="dummyfile").exists())




    



