from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import SecurityRecord


# Create your tests here.
class SecurityRecordAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="TestUser", password="TestPassword"
        )
        self.token = Token.objects.create(user=self.user)
        self.record = SecurityRecord.objects.create(
            name="Test Record", description="Test Description"
        )

    ###################################################
    ###### Test Access for Unauthenticated Users ######
    ###################################################
    def test_list_records_unauthenticated(self):
        # Ensure unauthenticated users cannot list security records
        url = reverse("securityrecord-list")
        self.client.credentials(HTTP_AUTHORIZATION="Token" + self.token.key)
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_record_unauthenticated(self):
        # Ensure unauthenticated users cannot retrieve a security record by ID
        url = reverse("securityrecord-detail", args=[self.record.pk])
        self.client.credentials(HTTP_AUTHORIZATION="Token" + self.token.key)
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_record_unauthenticated(self):
        # Ensure unauthenticated users cannot create a new security record
        url = reverse("securityrecord-list")
        data = {
            "name": "New Test Security Record",
            "description": "Description of the new Test security record.",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_record_unauthenticated(self):
        # Ensure unauthenticated users cannot update a security record
        url = reverse("securityrecord-detail", args=[self.record.pk])
        data = {
            "name": "Updated Test Record",
            "description": "Updated description of test security record.",
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_record_unauthenticated(self):
        # Ensure unauthenticated users cannot delete a security record
        url = reverse("securityrecord-detail", args=[self.record.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    #################################################
    ###### Test Access for Authenticated Users ######
    #################################################
    def test_list_records_authenticated(self):
        # Ensure authenticated users can list security records
        url = reverse("securityrecord-list")
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_record_authenticated(self):
        # Ensure authenticated users can retrieve a security record by ID
        url = reverse("securityrecord-detail", args=[self.record.pk])
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_record_authenticated(self):
        # Ensure authenticated users can create a new security record
        url = reverse("securityrecord-list")
        data = {
            "name": "New Test Security Record",
            "description": "Description of the new Test security record.",
        }
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_record_authenticated(self):
        # Ensure authenticated users can update a security record
        url = reverse("securityrecord-detail", args=[self.record.pk])
        data = {
            "name": "Updated Test Record",
            "description": "Updated description of test security record.",
        }
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_record_authenticated(self):
        # Ensure authenticated users can delete a security record
        url = reverse("securityrecord-detail", args=[self.record.pk])
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
