from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
#from .models import Employee

class AccountTests(APITestCase):
    def test_list_employess(self):
        """
        Ensure that we can list all employees.
        """
        url = '/employee/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_not_found_url(self):
        """
        Ensure that it returns that the page does not exist.
        """
        url = '/wemployee/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_access_denied(self):
        """
        Make sure that access is denied.
        """
        url = '/employee/'
        data = [
            {
                "name": "Mauricio Alegretti",
                "email": "mauricio.alegretti@igs-software.com.br",
                "department": "RH"
            }
        ]
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)