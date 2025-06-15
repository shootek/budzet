from django.test import TestCase
from django.urls import reverse
from .models import Entry, Category
from django.utils import timezone
from unittest.mock import patch

class HomeViewTests(TestCase):
    def test_home_view_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Budżet domowy")

class AddEntryViewTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Testowa kategoria")

    def test_add_entry_get(self):
        response = self.client.get(reverse('add_entry'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dodaj wpis")

    @patch('captcha.fields.CaptchaField.clean') 
    def test_add_entry_post_valid(self, mock_clean):
        mock_clean.return_value = 'Passed'

        response = self.client.post(reverse('add_entry'), {
            'type': 'income',
            'amount': '100.00',
            'category': self.category.id,
            'date': timezone.now().date(),
            'description': 'Testowy wpis',
            'captcha_0': 'test',
            'captcha_1': 'PASSED',
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Budżet domowy")
        self.assertEqual(Entry.objects.count(), 1)
