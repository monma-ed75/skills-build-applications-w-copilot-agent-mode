from rest_framework.test import APITestCase
from django.urls import reverse


class TrackerAPITests(APITestCase):
    def test_api_root(self):
        url = reverse('api-root')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('users', response.data)

    def test_users_endpoint(self):
        url = '/api/users/'
        response = self.client.get(url)
        # should return 200 even if empty
        self.assertIn(response.status_code, (200, 403))

    def test_teams_endpoint(self):
        url = '/api/teams/'
        response = self.client.get(url)
        self.assertIn(response.status_code, (200, 403))

    def test_activities_endpoint(self):
        url = '/api/activities/'
        response = self.client.get(url)
        self.assertIn(response.status_code, (200, 403))