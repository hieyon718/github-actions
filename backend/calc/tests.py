from django.test import TestCase
from django.urls import reverse

class AddAPITest(TestCase):
    def test_add_success(self):
        response = self.client.get('/add/?num1=1&num2=2')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['result'], 3)
    def test_add_invalid(self):
        response = self.client.get('/add/?num1=a&num2=2')
        
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())